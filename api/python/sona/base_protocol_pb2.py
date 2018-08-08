# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base_protocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='base_protocol.proto',
  package='protocol',
  serialized_pb=_b('\n\x13\x62\x61se_protocol.proto\x12\x08protocol\"\"\n\x0cKeepUsingReq\x12\x12\n\nserviceKey\x18\x01 \x02(\t\"\"\n\x0cSubscribeReq\x12\x12\n\nserviceKey\x18\x01 \x02(\t\"x\n\x12SubscribeBrokerRsp\x12\x12\n\nserviceKey\x18\x01 \x02(\t\x12\x0c\n\x04\x63ode\x18\x02 \x02(\x05\x12\x0f\n\x07version\x18\x03 \x02(\r\x12\x10\n\x08\x63onfKeys\x18\x04 \x03(\t\x12\x0e\n\x06values\x18\x05 \x03(\t\x12\r\n\x05\x65rror\x18\x06 \x01(\t\"D\n\x11SubscribeAgentRsp\x12\x12\n\nserviceKey\x18\x01 \x02(\t\x12\x0c\n\x04\x63ode\x18\x02 \x02(\x05\x12\r\n\x05index\x18\x03 \x01(\r\"]\n\x14PushServiceConfigReq\x12\x12\n\nserviceKey\x18\x01 \x02(\t\x12\x0f\n\x07version\x18\x02 \x02(\r\x12\x10\n\x08\x63onfKeys\x18\x03 \x03(\t\x12\x0e\n\x06values\x18\x04 \x03(\t\";\n\x14PullServiceConfigReq\x12\x12\n\nserviceKey\x18\x01 \x02(\t\x12\x0f\n\x07version\x18\x02 \x02(\r\"]\n\x14PullServiceConfigRsp\x12\x12\n\nserviceKey\x18\x01 \x02(\t\x12\x0f\n\x07version\x18\x02 \x02(\r\x12\x10\n\x08\x63onfKeys\x18\x03 \x03(\t\x12\x0e\n\x06values\x18\x04 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_KEEPUSINGREQ = _descriptor.Descriptor(
  name='KeepUsingReq',
  full_name='protocol.KeepUsingReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceKey', full_name='protocol.KeepUsingReq.serviceKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=67,
)


_SUBSCRIBEREQ = _descriptor.Descriptor(
  name='SubscribeReq',
  full_name='protocol.SubscribeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceKey', full_name='protocol.SubscribeReq.serviceKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=103,
)


_SUBSCRIBEBROKERRSP = _descriptor.Descriptor(
  name='SubscribeBrokerRsp',
  full_name='protocol.SubscribeBrokerRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceKey', full_name='protocol.SubscribeBrokerRsp.serviceKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='protocol.SubscribeBrokerRsp.code', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='protocol.SubscribeBrokerRsp.version', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confKeys', full_name='protocol.SubscribeBrokerRsp.confKeys', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='protocol.SubscribeBrokerRsp.values', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='protocol.SubscribeBrokerRsp.error', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=225,
)


_SUBSCRIBEAGENTRSP = _descriptor.Descriptor(
  name='SubscribeAgentRsp',
  full_name='protocol.SubscribeAgentRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceKey', full_name='protocol.SubscribeAgentRsp.serviceKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='protocol.SubscribeAgentRsp.code', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='protocol.SubscribeAgentRsp.index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=295,
)


_PUSHSERVICECONFIGREQ = _descriptor.Descriptor(
  name='PushServiceConfigReq',
  full_name='protocol.PushServiceConfigReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceKey', full_name='protocol.PushServiceConfigReq.serviceKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='protocol.PushServiceConfigReq.version', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confKeys', full_name='protocol.PushServiceConfigReq.confKeys', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='protocol.PushServiceConfigReq.values', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=390,
)


_PULLSERVICECONFIGREQ = _descriptor.Descriptor(
  name='PullServiceConfigReq',
  full_name='protocol.PullServiceConfigReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceKey', full_name='protocol.PullServiceConfigReq.serviceKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='protocol.PullServiceConfigReq.version', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=451,
)


_PULLSERVICECONFIGRSP = _descriptor.Descriptor(
  name='PullServiceConfigRsp',
  full_name='protocol.PullServiceConfigRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceKey', full_name='protocol.PullServiceConfigRsp.serviceKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='protocol.PullServiceConfigRsp.version', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confKeys', full_name='protocol.PullServiceConfigRsp.confKeys', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='protocol.PullServiceConfigRsp.values', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=546,
)

DESCRIPTOR.message_types_by_name['KeepUsingReq'] = _KEEPUSINGREQ
DESCRIPTOR.message_types_by_name['SubscribeReq'] = _SUBSCRIBEREQ
DESCRIPTOR.message_types_by_name['SubscribeBrokerRsp'] = _SUBSCRIBEBROKERRSP
DESCRIPTOR.message_types_by_name['SubscribeAgentRsp'] = _SUBSCRIBEAGENTRSP
DESCRIPTOR.message_types_by_name['PushServiceConfigReq'] = _PUSHSERVICECONFIGREQ
DESCRIPTOR.message_types_by_name['PullServiceConfigReq'] = _PULLSERVICECONFIGREQ
DESCRIPTOR.message_types_by_name['PullServiceConfigRsp'] = _PULLSERVICECONFIGRSP

KeepUsingReq = _reflection.GeneratedProtocolMessageType('KeepUsingReq', (_message.Message,), dict(
  DESCRIPTOR = _KEEPUSINGREQ,
  __module__ = 'base_protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.KeepUsingReq)
  ))
_sym_db.RegisterMessage(KeepUsingReq)

SubscribeReq = _reflection.GeneratedProtocolMessageType('SubscribeReq', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEREQ,
  __module__ = 'base_protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.SubscribeReq)
  ))
_sym_db.RegisterMessage(SubscribeReq)

SubscribeBrokerRsp = _reflection.GeneratedProtocolMessageType('SubscribeBrokerRsp', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEBROKERRSP,
  __module__ = 'base_protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.SubscribeBrokerRsp)
  ))
_sym_db.RegisterMessage(SubscribeBrokerRsp)

SubscribeAgentRsp = _reflection.GeneratedProtocolMessageType('SubscribeAgentRsp', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEAGENTRSP,
  __module__ = 'base_protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.SubscribeAgentRsp)
  ))
_sym_db.RegisterMessage(SubscribeAgentRsp)

PushServiceConfigReq = _reflection.GeneratedProtocolMessageType('PushServiceConfigReq', (_message.Message,), dict(
  DESCRIPTOR = _PUSHSERVICECONFIGREQ,
  __module__ = 'base_protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PushServiceConfigReq)
  ))
_sym_db.RegisterMessage(PushServiceConfigReq)

PullServiceConfigReq = _reflection.GeneratedProtocolMessageType('PullServiceConfigReq', (_message.Message,), dict(
  DESCRIPTOR = _PULLSERVICECONFIGREQ,
  __module__ = 'base_protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PullServiceConfigReq)
  ))
_sym_db.RegisterMessage(PullServiceConfigReq)

PullServiceConfigRsp = _reflection.GeneratedProtocolMessageType('PullServiceConfigRsp', (_message.Message,), dict(
  DESCRIPTOR = _PULLSERVICECONFIGRSP,
  __module__ = 'base_protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PullServiceConfigRsp)
  ))
_sym_db.RegisterMessage(PullServiceConfigRsp)


# @@protoc_insertion_point(module_scope)