# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: securedexchange.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='securedexchange.proto',
  package='securedexchange',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15securedexchange.proto\x12\x0fsecuredexchange\"9\n\x05Model\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0e\n\x06length\x18\x02 \x01(\x04\x12\x12\n\ninput_fact\x18\x03 \x03(\x05\"\x15\n\x04\x44\x61ta\x12\r\n\x05input\x18\x01 \x03(\x02\"R\n\x0bModelResult\x12\x16\n\x0e\x63lassification\x18\x01 \x01(\x05\x12\x12\n\nprediction\x18\x02 \x01(\x02\x12\n\n\x02ok\x18\x03 \x01(\x08\x12\x0b\n\x03msg\x18\x04 \x01(\t\"&\n\x0bSimpleReply\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x0b\n\x03msg\x18\x02 \x01(\t2\x92\x01\n\x08\x45xchange\x12\x43\n\tSendModel\x12\x16.securedexchange.Model\x1a\x1c.securedexchange.SimpleReply(\x01\x12\x41\n\x08SendData\x12\x15.securedexchange.Data\x1a\x1c.securedexchange.ModelResult(\x01\x62\x06proto3'
)




_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='securedexchange.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='securedexchange.Model.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='securedexchange.Model.length', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_fact', full_name='securedexchange.Model.input_fact', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=99,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='securedexchange.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='securedexchange.Data.input', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=122,
)


_MODELRESULT = _descriptor.Descriptor(
  name='ModelResult',
  full_name='securedexchange.ModelResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification', full_name='securedexchange.ModelResult.classification', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='securedexchange.ModelResult.prediction', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ok', full_name='securedexchange.ModelResult.ok', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='securedexchange.ModelResult.msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=206,
)


_SIMPLEREPLY = _descriptor.Descriptor(
  name='SimpleReply',
  full_name='securedexchange.SimpleReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='securedexchange.SimpleReply.ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='securedexchange.SimpleReply.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['ModelResult'] = _MODELRESULT
DESCRIPTOR.message_types_by_name['SimpleReply'] = _SIMPLEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'securedexchange_pb2'
  # @@protoc_insertion_point(class_scope:securedexchange.Model)
  })
_sym_db.RegisterMessage(Model)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'securedexchange_pb2'
  # @@protoc_insertion_point(class_scope:securedexchange.Data)
  })
_sym_db.RegisterMessage(Data)

ModelResult = _reflection.GeneratedProtocolMessageType('ModelResult', (_message.Message,), {
  'DESCRIPTOR' : _MODELRESULT,
  '__module__' : 'securedexchange_pb2'
  # @@protoc_insertion_point(class_scope:securedexchange.ModelResult)
  })
_sym_db.RegisterMessage(ModelResult)

SimpleReply = _reflection.GeneratedProtocolMessageType('SimpleReply', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEREPLY,
  '__module__' : 'securedexchange_pb2'
  # @@protoc_insertion_point(class_scope:securedexchange.SimpleReply)
  })
_sym_db.RegisterMessage(SimpleReply)



_EXCHANGE = _descriptor.ServiceDescriptor(
  name='Exchange',
  full_name='securedexchange.Exchange',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=249,
  serialized_end=395,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendModel',
    full_name='securedexchange.Exchange.SendModel',
    index=0,
    containing_service=None,
    input_type=_MODEL,
    output_type=_SIMPLEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendData',
    full_name='securedexchange.Exchange.SendData',
    index=1,
    containing_service=None,
    input_type=_DATA,
    output_type=_MODELRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXCHANGE)

DESCRIPTOR.services_by_name['Exchange'] = _EXCHANGE

# @@protoc_insertion_point(module_scope)