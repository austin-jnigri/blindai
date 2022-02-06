extern crate env_logger;
extern crate image;
extern crate sgx_libc;
extern crate sgx_tseal;
extern crate sgx_types;
extern crate tract_core;
extern crate tract_onnx;

use std::convert::TryInto;
use std::ops::DerefMut;
use std::mem::size_of;
use std::path::Path;
use std::ptr;
use std::slice;
use std::sync::{Arc, SgxMutex as Mutex};
use std::untrusted::fs::read;
use std::untrusted::fs::{metadata, read_dir, File};
use std::vec::Vec;
use log::*;

use futures::{Stream, StreamExt};
use image::{ImageBuffer, Rgb};
use rpc::untrusted_local_app_client::*;
use secured_exchange::exchange_server::{Exchange, ExchangeServer};
use secured_exchange::{Model, Data, ModelResult, SimpleReply};
use tokio::runtime;
use tokio::sync::mpsc;
use tokio_stream::wrappers::ReceiverStream;
use tonic::codegen::http::request;
use tonic::{
    transport::{Identity, Server},
    Request, Response, Status,
};
use tract_core::internal::*;
use tract_core::ops::matmul::lir_unary::*;
use tract_core::ops::{cnn, nn};
use tract_onnx::prelude::*;
use tract_onnx::prelude::tract_ndarray::IxDynImpl;

pub mod secured_exchange {
    tonic::include_proto!("securedexchange");
}

pub type OnnxModel = SimplePlan<TypedFact, Box<dyn TypedOp>, Graph<TypedFact, Box<dyn TypedOp>>>;

fn load_model(model: Vec<u8>, input_fact: Vec<i32>) -> TractResult<OnnxModel> {
    let mut model_slice = &model[..];
    let model_rec = tract_onnx::onnx()
        // load the model
        .model_for_read(&mut model_slice)?
        // specify input type and shape
        .with_input_fact(
            0,
            InferenceFact::dt_shape(f32::datum_type(), input_fact),
        )?
        // optimize the model
        .into_optimized()?
        // make the model runnable and fix its inputs and outputs
        .into_runnable()?;
    Ok(model_rec)
}

fn run_inference(model: &OnnxModel, input: Vec<f32>, input_fact: &Vec<usize>) -> TractResult<(f32, i32)>
{
    let dim = IxDynImpl::from(input_fact.as_slice());
    let image: Tensor = tract_ndarray::ArrayD::from_shape_vec(dim, input)?.into();
    let result = model.run(tvec!(image))?;
    let best = result[0]
        .to_array_view::<f32>()?
        .iter()
        .cloned()
        .zip(2..)
        .max_by(|a, b| a.0.partial_cmp(&b.0).unwrap()).unwrap();
    return Ok(best)
}

#[derive(Debug, Default)]
pub(crate) struct Exchanger 
{
    pub model: std::sync::Arc<Mutex<Option<OnnxModel>>>,
    pub input_fact: std::sync::Arc<Mutex<Vec<usize>>>,
    pub max_model_size: usize,
    pub max_input_size: usize
}

impl Exchanger {
    pub fn new(max_model_size: usize, max_input_size: usize) -> Self {
        Self {
            model: Arc::new(Mutex::new(None)),
            input_fact: Arc::new(Mutex::new(Vec::new())),
            max_model_size: max_model_size,
            max_input_size: max_input_size
        }
    }
}

#[tonic::async_trait]
impl Exchange for Exchanger {
    async fn send_model(
        &self,
        request: Request<tonic::Streaming<Model>>,
    ) -> Result<Response<SimpleReply>, Status> {
        let mut reply = SimpleReply::default();
        let mut stream = request.into_inner();
        let mut model_proto = Model::default();

        let mut input_fact: Vec<usize> = Vec::new();
        let mut model_bytes: Vec<u8> = Vec::new();
        let max_model_size = self.max_model_size;
        let mut model_size: usize = 0;

        while let Some(model_stream) = stream.next().await 
        {
            model_proto = model_stream?;
            if model_size == 0 {
                model_size = model_proto.length.try_into().unwrap();
            }
            if input_fact.len() == 0 {
                for x in &model_proto.input_fact 
                {
                    input_fact.push(*x as usize);
                }
            }
            if model_size > max_model_size || model_bytes.len() > max_model_size {
                error!("Incoming model is too big");
                return Err(Status::invalid_argument(format!("Model too big")))
            }
            model_bytes.append(&mut model_proto.data);
        }

        match load_model(model_bytes, model_proto.input_fact.clone()) {
            Ok(model_rec) => 
            {
                *self.model.lock().unwrap() = Some(model_rec);
                let input = &mut *self.input_fact.lock().unwrap();
                input.clear();
                input.append(&mut input_fact);
                reply.ok = true;
                reply.msg = format!("OK");
                info!("Model loaded successfully");
            }
            Err(_x) => 
            {
                reply.ok = false;
                reply.msg = format!("Failed to load model, error 02");
                error!("Failed to load model, the model is most likely invalid");
            }
        }
        Ok(Response::new(reply))
    }

    async fn send_data(
        &self,
        request: Request<tonic::Streaming<Data>>,
    ) -> Result<Response<ModelResult>, Status> {
        let mut reply = ModelResult::default();
        let mut stream = request.into_inner();
        let mut data_proto = Data::default();

        let mut input: Vec<f32> = Vec::new();
        let max_input_size = self.max_input_size;

        while let Some(data_stream) = stream.next().await 
        {
            data_proto = data_stream?;
            if data_proto.input.len() * size_of::<f32>() > max_input_size.try_into().unwrap() || input.len() * size_of::<f32>() > max_input_size {
                error!("Incoming input is too big");
                return Err(Status::invalid_argument(format!("Input too big")))
            }
            input.append(&mut data_proto.input);
        }

        let input_fact = &*self.input_fact.lock().unwrap();
        if let Some(model) = &*self.model.lock().unwrap() 
        {
            match run_inference(&model, input, &input_fact) { 
                Ok (tuple_res) => {
                    reply.prediction = tuple_res.0;
                    reply.classification = tuple_res.1;
                    reply.ok = true;
                    reply.msg = String::from("OK");
                    info!("Inference done successfully, sending encrypted result to the client");
                }
                Err (_) => 
                {
                    reply.ok = false;
                    reply.msg = String::from("Error while running the model");
                    error!("Error while running the inference");
                }
            }
        }
        else {
            reply.ok = false;
            reply.msg = String::from("Model not loaded, cannot continue");
            error!("Model not loaded, cannot run inference");
            return Ok(Response::new(reply));
        }
        Ok(Response::new(reply))
    }
}