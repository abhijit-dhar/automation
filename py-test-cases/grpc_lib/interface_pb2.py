# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interface.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import grpc_lib.common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='interface.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0finterface.proto\x1a\x0c\x63ommon.proto\"v\n\x0fInterfaceConfig\x12\x14\n\x0cinterface_id\x18\x01 \x01(\r\x12\x0b\n\x03mac\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0c\n\x04mask\x18\x04 \x01(\r\x12\n\n\x02gw\x18\x05 \x01(\t\x12\x1a\n\x05vlans\x18\x06 \x03(\x0b\x32\x0b.VlanConfig\">\n\nVlanConfig\x12\x0f\n\x07vlan_id\x18\x01 \x01(\r\x12\r\n\x05tp_id\x18\x02 \x01(\r\x12\x10\n\x08priority\x18\x03 \x01(\r\"\x8a\x01\n\x16InterfaceConfigRequest\x12\x1f\n\x07request\x18\x01 \x01(\x0b\x32\x0e.ConfigRequest\x12 \n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x10.InterfaceConfig\x12\r\n\x05\x63ount\x18\x03 \x01(\r\x12\x1e\n\x04step\x18\x04 \x01(\x0b\x32\x10.InterfaceConfig2M\n\tInterface\x12@\n\x12\x43onfigureInterface\x12\x17.InterfaceConfigRequest\x1a\x0f.StatusResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_INTERFACECONFIG = _descriptor.Descriptor(
  name='InterfaceConfig',
  full_name='InterfaceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface_id', full_name='InterfaceConfig.interface_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mac', full_name='InterfaceConfig.mac', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='InterfaceConfig.ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask', full_name='InterfaceConfig.mask', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gw', full_name='InterfaceConfig.gw', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vlans', full_name='InterfaceConfig.vlans', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=33,
  serialized_end=151,
)


_VLANCONFIG = _descriptor.Descriptor(
  name='VlanConfig',
  full_name='VlanConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vlan_id', full_name='VlanConfig.vlan_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tp_id', full_name='VlanConfig.tp_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='priority', full_name='VlanConfig.priority', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=153,
  serialized_end=215,
)


_INTERFACECONFIGREQUEST = _descriptor.Descriptor(
  name='InterfaceConfigRequest',
  full_name='InterfaceConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='InterfaceConfigRequest.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='InterfaceConfigRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='InterfaceConfigRequest.count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='step', full_name='InterfaceConfigRequest.step', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=218,
  serialized_end=356,
)

_INTERFACECONFIG.fields_by_name['vlans'].message_type = _VLANCONFIG
_INTERFACECONFIGREQUEST.fields_by_name['request'].message_type = common__pb2._CONFIGREQUEST
_INTERFACECONFIGREQUEST.fields_by_name['config'].message_type = _INTERFACECONFIG
_INTERFACECONFIGREQUEST.fields_by_name['step'].message_type = _INTERFACECONFIG
DESCRIPTOR.message_types_by_name['InterfaceConfig'] = _INTERFACECONFIG
DESCRIPTOR.message_types_by_name['VlanConfig'] = _VLANCONFIG
DESCRIPTOR.message_types_by_name['InterfaceConfigRequest'] = _INTERFACECONFIGREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InterfaceConfig = _reflection.GeneratedProtocolMessageType('InterfaceConfig', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACECONFIG,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:InterfaceConfig)
  })
_sym_db.RegisterMessage(InterfaceConfig)

VlanConfig = _reflection.GeneratedProtocolMessageType('VlanConfig', (_message.Message,), {
  'DESCRIPTOR' : _VLANCONFIG,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:VlanConfig)
  })
_sym_db.RegisterMessage(VlanConfig)

InterfaceConfigRequest = _reflection.GeneratedProtocolMessageType('InterfaceConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACECONFIGREQUEST,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:InterfaceConfigRequest)
  })
_sym_db.RegisterMessage(InterfaceConfigRequest)



_INTERFACE = _descriptor.ServiceDescriptor(
  name='Interface',
  full_name='Interface',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=358,
  serialized_end=435,
  methods=[
  _descriptor.MethodDescriptor(
    name='ConfigureInterface',
    full_name='Interface.ConfigureInterface',
    index=0,
    containing_service=None,
    input_type=_INTERFACECONFIGREQUEST,
    output_type=common__pb2._STATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INTERFACE)

DESCRIPTOR.services_by_name['Interface'] = _INTERFACE

# @@protoc_insertion_point(module_scope)
