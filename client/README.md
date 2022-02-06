# BlindAI Client

BlindAI Client is a python library to create client applications for BlindAI Server (Mithril-security's confidential inference server). 

## Installation

### Using pip
```bash
$ pip install blindai
```
## Usage

### Uploading a model

```python
from blindai.client import BlindAiClient

#Create the connection
client = BlindAiClient()
client.connect_server(
    "localhost",
    certificate="host_server.pem",
    simulation=True
)

#Upload the model to the server
response = client.upload_model(model="./mobilenetv2-7.onnx", shape=(1, 3, 224, 224))
```
### Uploading data
```python
from blindai.client import BlindAiClient
from PIL import Image
import numpy as np

#Create the connection
client = BlindAiClient()
client.connect_server(
    "localhost",
    certificate="host_server.pem",
    simulation=True
)

image = Image.open("grace_hopper.jpg").resize((224,224))
a = np.asarray(image, dtype=float)

#Send data for inference
result = client.send_data(a.flatten())
```

In order to connect to the BlindAI server, the client needs to acquire the following files from the server: 

- **policy.toml :** the enclave security policy that defines which enclave is trusted (if you are not using the simulation mode).

- **host_server.pem :** TLS certificate for the connection to the untrusted (app) part of the server.

**Simulation mode** enables to pypass the process of requesting and checking the attestation.

Usage examples can be found in [tutorial](./tutorial) folder.

Before you run an example, make sure to get `policy.toml`(if you are not using the simulation mode)  and `host_server.pem` that are generated in the server side. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License