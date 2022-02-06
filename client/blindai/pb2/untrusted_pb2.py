# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: untrusted.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='untrusted.proto',
  package='untrusted',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0funtrusted.proto\x12\tuntrusted\"\x17\n\x15GetCertificateRequest\"6\n\x13GetCertificateReply\x12\x1f\n\x17\x65nclave_tls_certificate\x18\x01 \x01(\x0c\"\x11\n\x0fGetTokenRequest\"\"\n GetSgxQuoteWithCollateralRequest\"\x1e\n\rGetTokenReply\x12\r\n\x05token\x18\x01 \x01(\t\"x\n\x1eGetSgxQuoteWithCollateralReply\x12\r\n\x05quote\x18\x01 \x01(\x0c\x12,\n\ncollateral\x18\x02 \x01(\x0b\x32\x18.untrusted.SgxCollateral\x12\x19\n\x11\x65nclave_held_data\x18\x03 \x01(\x0c\"\x80\x02\n\rSgxCollateral\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x1c\n\x14pck_crl_issuer_chain\x18\x02 \x01(\t\x12\x13\n\x0broot_ca_crl\x18\x03 \x01(\t\x12\x0f\n\x07pck_crl\x18\x04 \x01(\t\x12\x1d\n\x15tcb_info_issuer_chain\x18\x05 \x01(\t\x12\x10\n\x08tcb_info\x18\x06 \x01(\t\x12 \n\x18qe_identity_issuer_chain\x18\x07 \x01(\t\x12\x13\n\x0bqe_identity\x18\x08 \x01(\t\x12\x17\n\x0fpck_certificate\x18\t \x01(\t\x12\x19\n\x11pck_signing_chain\x18\n \x01(\t2\x98\x02\n\x0b\x41ttestation\x12R\n\x0eGetCertificate\x12 .untrusted.GetCertificateRequest\x1a\x1e.untrusted.GetCertificateReply\x12@\n\x08GetToken\x12\x1a.untrusted.GetTokenRequest\x1a\x18.untrusted.GetTokenReply\x12s\n\x19GetSgxQuoteWithCollateral\x12+.untrusted.GetSgxQuoteWithCollateralRequest\x1a).untrusted.GetSgxQuoteWithCollateralReplyb\x06proto3'
)




_GETCERTIFICATEREQUEST = _descriptor.Descriptor(
  name='GetCertificateRequest',
  full_name='untrusted.GetCertificateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=30,
  serialized_end=53,
)


_GETCERTIFICATEREPLY = _descriptor.Descriptor(
  name='GetCertificateReply',
  full_name='untrusted.GetCertificateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enclave_tls_certificate', full_name='untrusted.GetCertificateReply.enclave_tls_certificate', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=55,
  serialized_end=109,
)


_GETTOKENREQUEST = _descriptor.Descriptor(
  name='GetTokenRequest',
  full_name='untrusted.GetTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=111,
  serialized_end=128,
)


_GETSGXQUOTEWITHCOLLATERALREQUEST = _descriptor.Descriptor(
  name='GetSgxQuoteWithCollateralRequest',
  full_name='untrusted.GetSgxQuoteWithCollateralRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=130,
  serialized_end=164,
)


_GETTOKENREPLY = _descriptor.Descriptor(
  name='GetTokenReply',
  full_name='untrusted.GetTokenReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='untrusted.GetTokenReply.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=166,
  serialized_end=196,
)


_GETSGXQUOTEWITHCOLLATERALREPLY = _descriptor.Descriptor(
  name='GetSgxQuoteWithCollateralReply',
  full_name='untrusted.GetSgxQuoteWithCollateralReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='quote', full_name='untrusted.GetSgxQuoteWithCollateralReply.quote', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collateral', full_name='untrusted.GetSgxQuoteWithCollateralReply.collateral', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enclave_held_data', full_name='untrusted.GetSgxQuoteWithCollateralReply.enclave_held_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=198,
  serialized_end=318,
)


_SGXCOLLATERAL = _descriptor.Descriptor(
  name='SgxCollateral',
  full_name='untrusted.SgxCollateral',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='untrusted.SgxCollateral.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pck_crl_issuer_chain', full_name='untrusted.SgxCollateral.pck_crl_issuer_chain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root_ca_crl', full_name='untrusted.SgxCollateral.root_ca_crl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pck_crl', full_name='untrusted.SgxCollateral.pck_crl', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tcb_info_issuer_chain', full_name='untrusted.SgxCollateral.tcb_info_issuer_chain', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tcb_info', full_name='untrusted.SgxCollateral.tcb_info', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qe_identity_issuer_chain', full_name='untrusted.SgxCollateral.qe_identity_issuer_chain', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qe_identity', full_name='untrusted.SgxCollateral.qe_identity', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pck_certificate', full_name='untrusted.SgxCollateral.pck_certificate', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pck_signing_chain', full_name='untrusted.SgxCollateral.pck_signing_chain', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=321,
  serialized_end=577,
)

_GETSGXQUOTEWITHCOLLATERALREPLY.fields_by_name['collateral'].message_type = _SGXCOLLATERAL
DESCRIPTOR.message_types_by_name['GetCertificateRequest'] = _GETCERTIFICATEREQUEST
DESCRIPTOR.message_types_by_name['GetCertificateReply'] = _GETCERTIFICATEREPLY
DESCRIPTOR.message_types_by_name['GetTokenRequest'] = _GETTOKENREQUEST
DESCRIPTOR.message_types_by_name['GetSgxQuoteWithCollateralRequest'] = _GETSGXQUOTEWITHCOLLATERALREQUEST
DESCRIPTOR.message_types_by_name['GetTokenReply'] = _GETTOKENREPLY
DESCRIPTOR.message_types_by_name['GetSgxQuoteWithCollateralReply'] = _GETSGXQUOTEWITHCOLLATERALREPLY
DESCRIPTOR.message_types_by_name['SgxCollateral'] = _SGXCOLLATERAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCertificateRequest = _reflection.GeneratedProtocolMessageType('GetCertificateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCERTIFICATEREQUEST,
  '__module__' : 'untrusted_pb2'
  # @@protoc_insertion_point(class_scope:untrusted.GetCertificateRequest)
  })
_sym_db.RegisterMessage(GetCertificateRequest)

GetCertificateReply = _reflection.GeneratedProtocolMessageType('GetCertificateReply', (_message.Message,), {
  'DESCRIPTOR' : _GETCERTIFICATEREPLY,
  '__module__' : 'untrusted_pb2'
  # @@protoc_insertion_point(class_scope:untrusted.GetCertificateReply)
  })
_sym_db.RegisterMessage(GetCertificateReply)

GetTokenRequest = _reflection.GeneratedProtocolMessageType('GetTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTOKENREQUEST,
  '__module__' : 'untrusted_pb2'
  # @@protoc_insertion_point(class_scope:untrusted.GetTokenRequest)
  })
_sym_db.RegisterMessage(GetTokenRequest)

GetSgxQuoteWithCollateralRequest = _reflection.GeneratedProtocolMessageType('GetSgxQuoteWithCollateralRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSGXQUOTEWITHCOLLATERALREQUEST,
  '__module__' : 'untrusted_pb2'
  # @@protoc_insertion_point(class_scope:untrusted.GetSgxQuoteWithCollateralRequest)
  })
_sym_db.RegisterMessage(GetSgxQuoteWithCollateralRequest)

GetTokenReply = _reflection.GeneratedProtocolMessageType('GetTokenReply', (_message.Message,), {
  'DESCRIPTOR' : _GETTOKENREPLY,
  '__module__' : 'untrusted_pb2'
  # @@protoc_insertion_point(class_scope:untrusted.GetTokenReply)
  })
_sym_db.RegisterMessage(GetTokenReply)

GetSgxQuoteWithCollateralReply = _reflection.GeneratedProtocolMessageType('GetSgxQuoteWithCollateralReply', (_message.Message,), {
  'DESCRIPTOR' : _GETSGXQUOTEWITHCOLLATERALREPLY,
  '__module__' : 'untrusted_pb2'
  # @@protoc_insertion_point(class_scope:untrusted.GetSgxQuoteWithCollateralReply)
  })
_sym_db.RegisterMessage(GetSgxQuoteWithCollateralReply)

SgxCollateral = _reflection.GeneratedProtocolMessageType('SgxCollateral', (_message.Message,), {
  'DESCRIPTOR' : _SGXCOLLATERAL,
  '__module__' : 'untrusted_pb2'
  # @@protoc_insertion_point(class_scope:untrusted.SgxCollateral)
  })
_sym_db.RegisterMessage(SgxCollateral)



_ATTESTATION = _descriptor.ServiceDescriptor(
  name='Attestation',
  full_name='untrusted.Attestation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=580,
  serialized_end=860,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCertificate',
    full_name='untrusted.Attestation.GetCertificate',
    index=0,
    containing_service=None,
    input_type=_GETCERTIFICATEREQUEST,
    output_type=_GETCERTIFICATEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetToken',
    full_name='untrusted.Attestation.GetToken',
    index=1,
    containing_service=None,
    input_type=_GETTOKENREQUEST,
    output_type=_GETTOKENREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSgxQuoteWithCollateral',
    full_name='untrusted.Attestation.GetSgxQuoteWithCollateral',
    index=2,
    containing_service=None,
    input_type=_GETSGXQUOTEWITHCOLLATERALREQUEST,
    output_type=_GETSGXQUOTEWITHCOLLATERALREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ATTESTATION)

DESCRIPTOR.services_by_name['Attestation'] = _ATTESTATION

# @@protoc_insertion_point(module_scope)