# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meter_usage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='meter_usage.proto',
  package='meterusage',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11meter_usage.proto\x12\nmeterusage\"\x03\n\x01_\"\'\n\x05Usage\x12\x0c\n\x04time\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x01\"*\n\x06Usages\x12 \n\x05usage\x18\x01 \x03(\x0b\x32\x11.meterusage.Usage2?\n\nMeterUsage\x12\x31\n\nListUsages\x12\r.meterusage._\x1a\x12.meterusage.Usages\"\x00\x62\x06proto3'
)




__ = _descriptor.Descriptor(
  name='_',
  full_name='meterusage._',
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
  serialized_start=33,
  serialized_end=36,
)


_USAGE = _descriptor.Descriptor(
  name='Usage',
  full_name='meterusage.Usage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='meterusage.Usage.time', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='meterusage.Usage.quantity', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=38,
  serialized_end=77,
)


_USAGES = _descriptor.Descriptor(
  name='Usages',
  full_name='meterusage.Usages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='usage', full_name='meterusage.Usages.usage', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=79,
  serialized_end=121,
)

_USAGES.fields_by_name['usage'].message_type = _USAGE
DESCRIPTOR.message_types_by_name['_'] = __
DESCRIPTOR.message_types_by_name['Usage'] = _USAGE
DESCRIPTOR.message_types_by_name['Usages'] = _USAGES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ = _reflection.GeneratedProtocolMessageType('_', (_message.Message,), {
  'DESCRIPTOR' : __,
  '__module__' : 'meter_usage_pb2'
  # @@protoc_insertion_point(class_scope:meterusage._)
  })
_sym_db.RegisterMessage(_)

Usage = _reflection.GeneratedProtocolMessageType('Usage', (_message.Message,), {
  'DESCRIPTOR' : _USAGE,
  '__module__' : 'meter_usage_pb2'
  # @@protoc_insertion_point(class_scope:meterusage.Usage)
  })
_sym_db.RegisterMessage(Usage)

Usages = _reflection.GeneratedProtocolMessageType('Usages', (_message.Message,), {
  'DESCRIPTOR' : _USAGES,
  '__module__' : 'meter_usage_pb2'
  # @@protoc_insertion_point(class_scope:meterusage.Usages)
  })
_sym_db.RegisterMessage(Usages)



_METERUSAGE = _descriptor.ServiceDescriptor(
  name='MeterUsage',
  full_name='meterusage.MeterUsage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=123,
  serialized_end=186,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListUsages',
    full_name='meterusage.MeterUsage.ListUsages',
    index=0,
    containing_service=None,
    input_type=__,
    output_type=_USAGES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_METERUSAGE)

DESCRIPTOR.services_by_name['MeterUsage'] = _METERUSAGE

# @@protoc_insertion_point(module_scope)