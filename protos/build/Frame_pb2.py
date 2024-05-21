# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Frame.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Errors_pb2 as Errors__pb2

from .Errors_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Frame.proto',
  package='Kinova.Api',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x46rame.proto\x12\nKinova.Api\x1a\x0c\x45rrors.proto\"<\n\x05\x46rame\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.Kinova.Api.Header\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"^\n\x06Header\x12\x12\n\nframe_info\x18\x01 \x01(\x07\x12\x14\n\x0cmessage_info\x18\x02 \x01(\x07\x12\x14\n\x0cservice_info\x18\x03 \x01(\x07\x12\x14\n\x0cpayload_info\x18\x04 \x01(\x07\"e\n\x05\x45rror\x12*\n\nerror_code\x18\x01 \x01(\x0e\x32\x16.Kinova.Api.ErrorCodes\x12\x16\n\x0e\x65rror_sub_code\x18\x02 \x01(\r\x12\x18\n\x10\x65rror_sub_string\x18\x03 \x01(\t*4\n\rHeaderVersion\x12\x0e\n\nRESERVED_0\x10\x00\x12\x13\n\x0f\x43URRENT_VERSION\x10\x01*\xa0\x01\n\nFrameTypes\x12\x0c\n\x08RESERVED\x10\x00\x12\x15\n\x11MSG_FRAME_REQUEST\x10\x01\x12\x11\n\rMSG_FRAME_RAW\x10\x02\x12\x16\n\x12MSG_FRAME_RESPONSE\x10\x03\x12\x1a\n\x16MSG_FRAME_NOTIFICATION\x10\x05\x12\x12\n\x0eMSG_FRAME_PING\x10\x07\x12\x12\n\x0eMSG_FRAME_PONG\x10\x08P\x00\x62\x06proto3')
  ,
  dependencies=[Errors__pb2.DESCRIPTOR,],
  public_dependencies=[Errors__pb2.DESCRIPTOR,])

_HEADERVERSION = _descriptor.EnumDescriptor(
  name='HeaderVersion',
  full_name='Kinova.Api.HeaderVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESERVED_0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURRENT_VERSION', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=302,
  serialized_end=354,
)
_sym_db.RegisterEnumDescriptor(_HEADERVERSION)

HeaderVersion = enum_type_wrapper.EnumTypeWrapper(_HEADERVERSION)
_FRAMETYPES = _descriptor.EnumDescriptor(
  name='FrameTypes',
  full_name='Kinova.Api.FrameTypes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESERVED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_FRAME_REQUEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_FRAME_RAW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_FRAME_RESPONSE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_FRAME_NOTIFICATION', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_FRAME_PING', index=5, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_FRAME_PONG', index=6, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=357,
  serialized_end=517,
)
_sym_db.RegisterEnumDescriptor(_FRAMETYPES)

FrameTypes = enum_type_wrapper.EnumTypeWrapper(_FRAMETYPES)
RESERVED_0 = 0
CURRENT_VERSION = 1
RESERVED = 0
MSG_FRAME_REQUEST = 1
MSG_FRAME_RAW = 2
MSG_FRAME_RESPONSE = 3
MSG_FRAME_NOTIFICATION = 5
MSG_FRAME_PING = 7
MSG_FRAME_PONG = 8



_FRAME = _descriptor.Descriptor(
  name='Frame',
  full_name='Kinova.Api.Frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Kinova.Api.Frame.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Kinova.Api.Frame.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=101,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='Kinova.Api.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_info', full_name='Kinova.Api.Header.frame_info', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_info', full_name='Kinova.Api.Header.message_info', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_info', full_name='Kinova.Api.Header.service_info', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload_info', full_name='Kinova.Api.Header.payload_info', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=197,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='Kinova.Api.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Kinova.Api.Error.error_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_sub_code', full_name='Kinova.Api.Error.error_sub_code', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_sub_string', full_name='Kinova.Api.Error.error_sub_string', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=300,
)

_FRAME.fields_by_name['header'].message_type = _HEADER
_ERROR.fields_by_name['error_code'].enum_type = Errors__pb2._ERRORCODES
DESCRIPTOR.message_types_by_name['Frame'] = _FRAME
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.enum_types_by_name['HeaderVersion'] = _HEADERVERSION
DESCRIPTOR.enum_types_by_name['FrameTypes'] = _FRAMETYPES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Frame = _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), dict(
  DESCRIPTOR = _FRAME,
  __module__ = 'Frame_pb2'
  # @@protoc_insertion_point(class_scope:Kinova.Api.Frame)
  ))
_sym_db.RegisterMessage(Frame)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'Frame_pb2'
  # @@protoc_insertion_point(class_scope:Kinova.Api.Header)
  ))
_sym_db.RegisterMessage(Header)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'Frame_pb2'
  # @@protoc_insertion_point(class_scope:Kinova.Api.Error)
  ))
_sym_db.RegisterMessage(Error)


# @@protoc_insertion_point(module_scope)