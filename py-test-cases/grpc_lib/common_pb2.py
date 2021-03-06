# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63ommon.proto\"\x1f\n\x0cStartRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\r\"\x1e\n\x0bStopRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\r\"m\n\x0eStatusResponse\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.StatusResponse.Status\"3\n\x06Status\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\"}\n\rConfigRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\r\x12!\n\x04type\x18\x02 \x01(\x0e\x32\x13.ConfigRequest.Type\"8\n\x04Type\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06MODIFY\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x62\x06proto3'
)



_STATUSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='StatusResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=139,
  serialized_end=190,
)
_sym_db.RegisterEnumDescriptor(_STATUSRESPONSE_STATUS)

_CONFIGREQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ConfigRequest.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODIFY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=261,
  serialized_end=317,
)
_sym_db.RegisterEnumDescriptor(_CONFIGREQUEST_TYPE)


_STARTREQUEST = _descriptor.Descriptor(
  name='StartRequest',
  full_name='StartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_id', full_name='StartRequest.port_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=16,
  serialized_end=47,
)


_STOPREQUEST = _descriptor.Descriptor(
  name='StopRequest',
  full_name='StopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_id', full_name='StopRequest.port_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=49,
  serialized_end=79,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='StatusResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUSRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=190,
)


_CONFIGREQUEST = _descriptor.Descriptor(
  name='ConfigRequest',
  full_name='ConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_id', full_name='ConfigRequest.port_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ConfigRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIGREQUEST_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=317,
)

_STATUSRESPONSE.fields_by_name['status'].enum_type = _STATUSRESPONSE_STATUS
_STATUSRESPONSE_STATUS.containing_type = _STATUSRESPONSE
_CONFIGREQUEST.fields_by_name['type'].enum_type = _CONFIGREQUEST_TYPE
_CONFIGREQUEST_TYPE.containing_type = _CONFIGREQUEST
DESCRIPTOR.message_types_by_name['StartRequest'] = _STARTREQUEST
DESCRIPTOR.message_types_by_name['StopRequest'] = _STOPREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['ConfigRequest'] = _CONFIGREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartRequest = _reflection.GeneratedProtocolMessageType('StartRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTREQUEST,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:StartRequest)
  })
_sym_db.RegisterMessage(StartRequest)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPREQUEST,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:StopRequest)
  })
_sym_db.RegisterMessage(StopRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)

ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGREQUEST,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:ConfigRequest)
  })
_sym_db.RegisterMessage(ConfigRequest)


# @@protoc_insertion_point(module_scope)
