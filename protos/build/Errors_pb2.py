# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Errors.proto

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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Errors.proto',
  package='Kinova.Api',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x45rrors.proto\x12\nKinova.Api*x\n\nErrorCodes\x12\x0e\n\nERROR_NONE\x10\x00\x12\x19\n\x15\x45RROR_PROTOCOL_SERVER\x10\x01\x12\x19\n\x15\x45RROR_PROTOCOL_CLIENT\x10\x02\x12\x10\n\x0c\x45RROR_DEVICE\x10\x03\x12\x12\n\x0e\x45RROR_INTERNAL\x10\x04*\xc9\x15\n\rSubErrorCodes\x12\x12\n\x0eSUB_ERROR_NONE\x10\x00\x12\x11\n\rMETHOD_FAILED\x10\x01\x12\x11\n\rUNIMPLEMENTED\x10\x02\x12\x11\n\rINVALID_PARAM\x10\x03\x12\x17\n\x13UNSUPPORTED_SERVICE\x10\x04\x12\x16\n\x12UNSUPPORTED_METHOD\x10\x05\x12\"\n\x1eTOO_LARGE_ENCODED_FRAME_BUFFER\x10\x06\x12\x16\n\x12\x46RAME_ENCODING_ERR\x10\x07\x12\x16\n\x12\x46RAME_DECODING_ERR\x10\x08\x12\x1f\n\x1bINCOMPATIBLE_HEADER_VERSION\x10\t\x12\x1a\n\x16UNSUPPORTED_FRAME_TYPE\x10\n\x12&\n\"UNREGISTERED_NOTIFICATION_RECEIVED\x10\x0b\x12\x13\n\x0fINVALID_SESSION\x10\x0c\x12\x18\n\x14PAYLOAD_DECODING_ERR\x10\r\x12\x1f\n\x1bUNREGISTERED_FRAME_RECEIVED\x10\x0e\x12\x14\n\x10INVALID_PASSWORD\x10\x0f\x12\x12\n\x0eUSER_NOT_FOUND\x10\x10\x12\x14\n\x10\x45NTITY_NOT_FOUND\x10\x11\x12\x1e\n\x1aROBOT_MOVEMENT_IN_PROGRESS\x10\x12\x12\x14\n\x10ROBOT_NOT_MOVING\x10\x13\x12\x19\n\x15NO_MORE_STORAGE_SPACE\x10\x14\x12\x13\n\x0fROBOT_NOT_READY\x10\x15\x12\x12\n\x0eROBOT_IN_FAULT\x10\x16\x12\x18\n\x14ROBOT_IN_MAINTENANCE\x10\x17\x12\x18\n\x14ROBOT_IN_UPDATE_MODE\x10\x18\x12\x1b\n\x17ROBOT_IN_EMERGENCY_STOP\x10\x19\x12\x19\n\x15SINGLE_LEVEL_SERVOING\x10\x1a\x12\x16\n\x12LOW_LEVEL_SERVOING\x10\x1b\x12\x1a\n\x16MAPPING_GROUP_NON_ROOT\x10\x1c\x12\x19\n\x15MAPPING_INVALID_GROUP\x10\x1d\x12\x17\n\x13MAPPING_INVALID_MAP\x10\x1e\x12\x19\n\x15MAP_GROUP_INVALID_MAP\x10\x1f\x12\x1c\n\x18MAP_GROUP_INVALID_PARENT\x10 \x12\x1b\n\x17MAP_GROUP_INVALID_CHILD\x10!\x12\x1a\n\x16MAP_GROUP_INVALID_MOVE\x10\"\x12\x0e\n\nMAP_IN_USE\x10#\x12\x16\n\x12WIFI_CONNECT_ERROR\x10$\x12\x1c\n\x18UNSUPPORTED_NETWORK_TYPE\x10%\x12$\n TOO_LARGE_ENCODED_PAYLOAD_BUFFER\x10&\x12\x1c\n\x18UPDATE_PERMISSION_DENIED\x10\'\x12\x1c\n\x18\x44\x45LETE_PERMISSION_DENIED\x10(\x12\x12\n\x0e\x44\x41TABASE_ERROR\x10)\x12\x16\n\x12UNSUPPORTED_OPTION\x10*\x12\x1a\n\x16UNSUPPORTED_RESOLUTION\x10+\x12\x1a\n\x16UNSUPPORTED_FRAME_RATE\x10,\x12\x18\n\x14UNSUPPORTED_BIT_RATE\x10-\x12\x16\n\x12UNSUPPORTED_ACTION\x10.\x12\x1c\n\x18UNSUPPORTED_FOCUS_ACTION\x10/\x12\x1a\n\x16VALUE_IS_ABOVE_MAXIMUM\x10\x30\x12\x1a\n\x16VALUE_IS_BELOW_MINIMUM\x10\x31\x12\x17\n\x13\x44\x45VICE_DISCONNECTED\x10\x32\x12\x14\n\x10\x44\x45VICE_NOT_READY\x10\x33\x12\x12\n\x0eINVALID_DEVICE\x10\x34\x12\x1c\n\x18SAFETY_THRESHOLD_REACHED\x10\x35\x12\x1f\n\x1bINVALID_USER_SESSION_ACCESS\x10\x36\x12\x17\n\x13\x43ONTROL_MANUAL_STOP\x10\x37\x12\x1d\n\x19\x43ONTROL_OUTSIDE_WORKSPACE\x10\x38\x12#\n\x1f\x43ONTROL_ACTUATOR_COUNT_MISMATCH\x10\x39\x12\x1c\n\x18\x43ONTROL_INVALID_DURATION\x10:\x12\x19\n\x15\x43ONTROL_INVALID_SPEED\x10;\x12\x17\n\x13\x43ONTROL_LARGE_SPEED\x10<\x12 \n\x1c\x43ONTROL_INVALID_ACCELERATION\x10=\x12\x1d\n\x19\x43ONTROL_INVALID_TIME_STEP\x10>\x12\x16\n\x12\x43ONTROL_LARGE_SIZE\x10?\x12\x16\n\x12\x43ONTROL_WRONG_MODE\x10@\x12 \n\x1c\x43ONTROL_JOINT_POSITION_LIMIT\x10\x41\x12\x1d\n\x19\x43ONTROL_NO_FILE_IN_MEMORY\x10\x42\x12#\n\x1f\x43ONTROL_INDEX_OUT_OF_TRAJECTORY\x10\x43\x12\x1b\n\x17\x43ONTROL_ALREADY_RUNNING\x10\x44\x12 \n\x1c\x43ONTROL_WRONG_STARTING_POINT\x10\x45\x12\"\n\x1e\x43ONTROL_CARTESIAN_CANNOT_START\x10\x46\x12 \n\x1c\x43ONTROL_UNDEFINED_CONSTRAINT\x10G\x12\x19\n\x15\x43ONTROL_UNINITIALIZED\x10H\x12\x15\n\x11\x43ONTROL_NO_ACTION\x10I\x12\x15\n\x11\x43ONTROL_UNDEFINED\x10J\x12\x17\n\x13WRONG_SERVOING_MODE\x10K\x12 \n\x1c\x43ONTROL_WRONG_STARTING_SPEED\x10L\x12\x1c\n\x18USERNAME_LENGTH_EXCEEDED\x10\x64\x12\x1d\n\x19\x46IRSTNAME_LENGTH_EXCEEDED\x10\x65\x12\x1c\n\x18LASTNAME_LENGTH_EXCEEDED\x10\x66\x12\x1c\n\x18PASSWORD_LENGTH_EXCEEDED\x10g\x12\x1b\n\x17USERNAME_ALREADY_EXISTS\x10h\x12\x12\n\x0eUSERNAME_EMPTY\x10i\x12\x18\n\x14PASSWORD_NOT_CHANGED\x10j\x12\x1e\n\x1aMAXIMUM_USER_PROFILES_USED\x10k\x12\x15\n\x11ROUTER_UNVAILABLE\x10l\x12\x1e\n\x1a\x41\x44\x44RESS_NOT_IN_VALID_RANGE\x10x\x12\x1c\n\x18\x41\x44\x44RESS_NOT_CONFIGURABLE\x10y\x12\x1b\n\x16SESSION_NOT_IN_CONTROL\x10\x82\x01\x12\x13\n\x0eMETHOD_TIMEOUT\x10\x83\x01\x12$\n\x1fUNSUPPORTED_ROBOT_CONFIGURATION\x10\x84\x01\x12\x14\n\x0fNVRAM_READ_FAIL\x10\x85\x01\x12\x15\n\x10NVRAM_WRITE_FAIL\x10\x86\x01\x12 \n\x1bNETWORK_NO_ADDRESS_ASSIGNED\x10\x87\x01\x12\x1b\n\x16READ_PERMISSION_DENIED\x10\x88\x01\x12\x1f\n\x1a\x43ONTROLLER_INVALID_MAPPING\x10\x89\x01\x12\x12\n\rACTION_IN_USE\x10\x8a\x01\x12\x10\n\x0bSEND_FAILED\x10\x8b\x01\x12(\n#CONTROL_WAYPOINT_TRAJECTORY_ABORTED\x10\x8c\x01\x12\x1e\n\x19\x43ONTROL_PERMISSION_DENIED\x10\x8d\x01\x62\x06proto3')
)

_ERRORCODES = _descriptor.EnumDescriptor(
  name='ErrorCodes',
  full_name='Kinova.Api.ErrorCodes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PROTOCOL_SERVER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PROTOCOL_CLIENT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_DEVICE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INTERNAL', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=28,
  serialized_end=148,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODES)

ErrorCodes = enum_type_wrapper.EnumTypeWrapper(_ERRORCODES)
_SUBERRORCODES = _descriptor.EnumDescriptor(
  name='SubErrorCodes',
  full_name='Kinova.Api.SubErrorCodes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUB_ERROR_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METHOD_FAILED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNIMPLEMENTED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARAM', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_SERVICE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_METHOD', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_LARGE_ENCODED_FRAME_BUFFER', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRAME_ENCODING_ERR', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRAME_DECODING_ERR', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOMPATIBLE_HEADER_VERSION', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_FRAME_TYPE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTERED_NOTIFICATION_RECEIVED', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SESSION', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYLOAD_DECODING_ERR', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTERED_FRAME_RECEIVED', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PASSWORD', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_NOT_FOUND', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTITY_NOT_FOUND', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_MOVEMENT_IN_PROGRESS', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_NOT_MOVING', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_MORE_STORAGE_SPACE', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_NOT_READY', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_IN_FAULT', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_IN_MAINTENANCE', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_IN_UPDATE_MODE', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_IN_EMERGENCY_STOP', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINGLE_LEVEL_SERVOING', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW_LEVEL_SERVOING', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAPPING_GROUP_NON_ROOT', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAPPING_INVALID_GROUP', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAPPING_INVALID_MAP', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_GROUP_INVALID_MAP', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_GROUP_INVALID_PARENT', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_GROUP_INVALID_CHILD', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_GROUP_INVALID_MOVE', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_IN_USE', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFI_CONNECT_ERROR', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_NETWORK_TYPE', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_LARGE_ENCODED_PAYLOAD_BUFFER', index=38, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_PERMISSION_DENIED', index=39, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_PERMISSION_DENIED', index=40, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATABASE_ERROR', index=41, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_OPTION', index=42, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_RESOLUTION', index=43, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_FRAME_RATE', index=44, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_BIT_RATE', index=45, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_ACTION', index=46, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_FOCUS_ACTION', index=47, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_IS_ABOVE_MAXIMUM', index=48, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_IS_BELOW_MINIMUM', index=49, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_DISCONNECTED', index=50, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_NOT_READY', index=51, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DEVICE', index=52, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAFETY_THRESHOLD_REACHED', index=53, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_USER_SESSION_ACCESS', index=54, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_MANUAL_STOP', index=55, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_OUTSIDE_WORKSPACE', index=56, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_ACTUATOR_COUNT_MISMATCH', index=57, number=57,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_INVALID_DURATION', index=58, number=58,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_INVALID_SPEED', index=59, number=59,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_LARGE_SPEED', index=60, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_INVALID_ACCELERATION', index=61, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_INVALID_TIME_STEP', index=62, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_LARGE_SIZE', index=63, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_WRONG_MODE', index=64, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_JOINT_POSITION_LIMIT', index=65, number=65,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_NO_FILE_IN_MEMORY', index=66, number=66,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_INDEX_OUT_OF_TRAJECTORY', index=67, number=67,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_ALREADY_RUNNING', index=68, number=68,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_WRONG_STARTING_POINT', index=69, number=69,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_CARTESIAN_CANNOT_START', index=70, number=70,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_UNDEFINED_CONSTRAINT', index=71, number=71,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_UNINITIALIZED', index=72, number=72,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_NO_ACTION', index=73, number=73,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_UNDEFINED', index=74, number=74,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_SERVOING_MODE', index=75, number=75,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_WRONG_STARTING_SPEED', index=76, number=76,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERNAME_LENGTH_EXCEEDED', index=77, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRSTNAME_LENGTH_EXCEEDED', index=78, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LASTNAME_LENGTH_EXCEEDED', index=79, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSWORD_LENGTH_EXCEEDED', index=80, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERNAME_ALREADY_EXISTS', index=81, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERNAME_EMPTY', index=82, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSWORD_NOT_CHANGED', index=83, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMUM_USER_PROFILES_USED', index=84, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTER_UNVAILABLE', index=85, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_NOT_IN_VALID_RANGE', index=86, number=120,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_NOT_CONFIGURABLE', index=87, number=121,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_NOT_IN_CONTROL', index=88, number=130,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METHOD_TIMEOUT', index=89, number=131,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_ROBOT_CONFIGURATION', index=90, number=132,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NVRAM_READ_FAIL', index=91, number=133,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NVRAM_WRITE_FAIL', index=92, number=134,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NETWORK_NO_ADDRESS_ASSIGNED', index=93, number=135,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_PERMISSION_DENIED', index=94, number=136,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROLLER_INVALID_MAPPING', index=95, number=137,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_IN_USE', index=96, number=138,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_FAILED', index=97, number=139,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_WAYPOINT_TRAJECTORY_ABORTED', index=98, number=140,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_PERMISSION_DENIED', index=99, number=141,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=151,
  serialized_end=2912,
)
_sym_db.RegisterEnumDescriptor(_SUBERRORCODES)

SubErrorCodes = enum_type_wrapper.EnumTypeWrapper(_SUBERRORCODES)
ERROR_NONE = 0
ERROR_PROTOCOL_SERVER = 1
ERROR_PROTOCOL_CLIENT = 2
ERROR_DEVICE = 3
ERROR_INTERNAL = 4
SUB_ERROR_NONE = 0
METHOD_FAILED = 1
UNIMPLEMENTED = 2
INVALID_PARAM = 3
UNSUPPORTED_SERVICE = 4
UNSUPPORTED_METHOD = 5
TOO_LARGE_ENCODED_FRAME_BUFFER = 6
FRAME_ENCODING_ERR = 7
FRAME_DECODING_ERR = 8
INCOMPATIBLE_HEADER_VERSION = 9
UNSUPPORTED_FRAME_TYPE = 10
UNREGISTERED_NOTIFICATION_RECEIVED = 11
INVALID_SESSION = 12
PAYLOAD_DECODING_ERR = 13
UNREGISTERED_FRAME_RECEIVED = 14
INVALID_PASSWORD = 15
USER_NOT_FOUND = 16
ENTITY_NOT_FOUND = 17
ROBOT_MOVEMENT_IN_PROGRESS = 18
ROBOT_NOT_MOVING = 19
NO_MORE_STORAGE_SPACE = 20
ROBOT_NOT_READY = 21
ROBOT_IN_FAULT = 22
ROBOT_IN_MAINTENANCE = 23
ROBOT_IN_UPDATE_MODE = 24
ROBOT_IN_EMERGENCY_STOP = 25
SINGLE_LEVEL_SERVOING = 26
LOW_LEVEL_SERVOING = 27
MAPPING_GROUP_NON_ROOT = 28
MAPPING_INVALID_GROUP = 29
MAPPING_INVALID_MAP = 30
MAP_GROUP_INVALID_MAP = 31
MAP_GROUP_INVALID_PARENT = 32
MAP_GROUP_INVALID_CHILD = 33
MAP_GROUP_INVALID_MOVE = 34
MAP_IN_USE = 35
WIFI_CONNECT_ERROR = 36
UNSUPPORTED_NETWORK_TYPE = 37
TOO_LARGE_ENCODED_PAYLOAD_BUFFER = 38
UPDATE_PERMISSION_DENIED = 39
DELETE_PERMISSION_DENIED = 40
DATABASE_ERROR = 41
UNSUPPORTED_OPTION = 42
UNSUPPORTED_RESOLUTION = 43
UNSUPPORTED_FRAME_RATE = 44
UNSUPPORTED_BIT_RATE = 45
UNSUPPORTED_ACTION = 46
UNSUPPORTED_FOCUS_ACTION = 47
VALUE_IS_ABOVE_MAXIMUM = 48
VALUE_IS_BELOW_MINIMUM = 49
DEVICE_DISCONNECTED = 50
DEVICE_NOT_READY = 51
INVALID_DEVICE = 52
SAFETY_THRESHOLD_REACHED = 53
INVALID_USER_SESSION_ACCESS = 54
CONTROL_MANUAL_STOP = 55
CONTROL_OUTSIDE_WORKSPACE = 56
CONTROL_ACTUATOR_COUNT_MISMATCH = 57
CONTROL_INVALID_DURATION = 58
CONTROL_INVALID_SPEED = 59
CONTROL_LARGE_SPEED = 60
CONTROL_INVALID_ACCELERATION = 61
CONTROL_INVALID_TIME_STEP = 62
CONTROL_LARGE_SIZE = 63
CONTROL_WRONG_MODE = 64
CONTROL_JOINT_POSITION_LIMIT = 65
CONTROL_NO_FILE_IN_MEMORY = 66
CONTROL_INDEX_OUT_OF_TRAJECTORY = 67
CONTROL_ALREADY_RUNNING = 68
CONTROL_WRONG_STARTING_POINT = 69
CONTROL_CARTESIAN_CANNOT_START = 70
CONTROL_UNDEFINED_CONSTRAINT = 71
CONTROL_UNINITIALIZED = 72
CONTROL_NO_ACTION = 73
CONTROL_UNDEFINED = 74
WRONG_SERVOING_MODE = 75
CONTROL_WRONG_STARTING_SPEED = 76
USERNAME_LENGTH_EXCEEDED = 100
FIRSTNAME_LENGTH_EXCEEDED = 101
LASTNAME_LENGTH_EXCEEDED = 102
PASSWORD_LENGTH_EXCEEDED = 103
USERNAME_ALREADY_EXISTS = 104
USERNAME_EMPTY = 105
PASSWORD_NOT_CHANGED = 106
MAXIMUM_USER_PROFILES_USED = 107
ROUTER_UNVAILABLE = 108
ADDRESS_NOT_IN_VALID_RANGE = 120
ADDRESS_NOT_CONFIGURABLE = 121
SESSION_NOT_IN_CONTROL = 130
METHOD_TIMEOUT = 131
UNSUPPORTED_ROBOT_CONFIGURATION = 132
NVRAM_READ_FAIL = 133
NVRAM_WRITE_FAIL = 134
NETWORK_NO_ADDRESS_ASSIGNED = 135
READ_PERMISSION_DENIED = 136
CONTROLLER_INVALID_MAPPING = 137
ACTION_IN_USE = 138
SEND_FAILED = 139
CONTROL_WAYPOINT_TRAJECTORY_ABORTED = 140
CONTROL_PERMISSION_DENIED = 141


DESCRIPTOR.enum_types_by_name['ErrorCodes'] = _ERRORCODES
DESCRIPTOR.enum_types_by_name['SubErrorCodes'] = _SUBERRORCODES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
