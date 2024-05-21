"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

KINOVA (R) KORTEX (TM)

Copyright (c) 2018 Kinova inc. All rights reserved.

This software may be modified and distributed
under the terms of the BSD 3-Clause license.

Refer to the LICENSE file for details.
"""
from . import Errors_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
from .Errors_pb2 import (
    ACTION_IN_USE as ACTION_IN_USE,
    ADDRESS_NOT_CONFIGURABLE as ADDRESS_NOT_CONFIGURABLE,
    ADDRESS_NOT_IN_VALID_RANGE as ADDRESS_NOT_IN_VALID_RANGE,
    CONTROLLER_INVALID_MAPPING as CONTROLLER_INVALID_MAPPING,
    CONTROL_ACTUATOR_COUNT_MISMATCH as CONTROL_ACTUATOR_COUNT_MISMATCH,
    CONTROL_ALREADY_RUNNING as CONTROL_ALREADY_RUNNING,
    CONTROL_CARTESIAN_CANNOT_START as CONTROL_CARTESIAN_CANNOT_START,
    CONTROL_INDEX_OUT_OF_TRAJECTORY as CONTROL_INDEX_OUT_OF_TRAJECTORY,
    CONTROL_INVALID_ACCELERATION as CONTROL_INVALID_ACCELERATION,
    CONTROL_INVALID_DURATION as CONTROL_INVALID_DURATION,
    CONTROL_INVALID_SPEED as CONTROL_INVALID_SPEED,
    CONTROL_INVALID_TIME_STEP as CONTROL_INVALID_TIME_STEP,
    CONTROL_JOINT_POSITION_LIMIT as CONTROL_JOINT_POSITION_LIMIT,
    CONTROL_LARGE_SIZE as CONTROL_LARGE_SIZE,
    CONTROL_LARGE_SPEED as CONTROL_LARGE_SPEED,
    CONTROL_MANUAL_STOP as CONTROL_MANUAL_STOP,
    CONTROL_NO_ACTION as CONTROL_NO_ACTION,
    CONTROL_NO_FILE_IN_MEMORY as CONTROL_NO_FILE_IN_MEMORY,
    CONTROL_OUTSIDE_WORKSPACE as CONTROL_OUTSIDE_WORKSPACE,
    CONTROL_PERMISSION_DENIED as CONTROL_PERMISSION_DENIED,
    CONTROL_UNDEFINED as CONTROL_UNDEFINED,
    CONTROL_UNDEFINED_CONSTRAINT as CONTROL_UNDEFINED_CONSTRAINT,
    CONTROL_UNINITIALIZED as CONTROL_UNINITIALIZED,
    CONTROL_WAYPOINT_TRAJECTORY_ABORTED as CONTROL_WAYPOINT_TRAJECTORY_ABORTED,
    CONTROL_WRONG_MODE as CONTROL_WRONG_MODE,
    CONTROL_WRONG_STARTING_POINT as CONTROL_WRONG_STARTING_POINT,
    CONTROL_WRONG_STARTING_SPEED as CONTROL_WRONG_STARTING_SPEED,
    DATABASE_ERROR as DATABASE_ERROR,
    DELETE_PERMISSION_DENIED as DELETE_PERMISSION_DENIED,
    DEVICE_DISCONNECTED as DEVICE_DISCONNECTED,
    DEVICE_NOT_READY as DEVICE_NOT_READY,
    ENTITY_NOT_FOUND as ENTITY_NOT_FOUND,
    ERROR_DEVICE as ERROR_DEVICE,
    ERROR_INTERNAL as ERROR_INTERNAL,
    ERROR_NONE as ERROR_NONE,
    ERROR_PROTOCOL_CLIENT as ERROR_PROTOCOL_CLIENT,
    ERROR_PROTOCOL_SERVER as ERROR_PROTOCOL_SERVER,
    ErrorCodes as ErrorCodes,
    FIRSTNAME_LENGTH_EXCEEDED as FIRSTNAME_LENGTH_EXCEEDED,
    FRAME_DECODING_ERR as FRAME_DECODING_ERR,
    FRAME_ENCODING_ERR as FRAME_ENCODING_ERR,
    INCOMPATIBLE_HEADER_VERSION as INCOMPATIBLE_HEADER_VERSION,
    INVALID_DEVICE as INVALID_DEVICE,
    INVALID_PARAM as INVALID_PARAM,
    INVALID_PASSWORD as INVALID_PASSWORD,
    INVALID_SESSION as INVALID_SESSION,
    INVALID_USER_SESSION_ACCESS as INVALID_USER_SESSION_ACCESS,
    LASTNAME_LENGTH_EXCEEDED as LASTNAME_LENGTH_EXCEEDED,
    LOW_LEVEL_SERVOING as LOW_LEVEL_SERVOING,
    MAPPING_GROUP_NON_ROOT as MAPPING_GROUP_NON_ROOT,
    MAPPING_INVALID_GROUP as MAPPING_INVALID_GROUP,
    MAPPING_INVALID_MAP as MAPPING_INVALID_MAP,
    MAP_GROUP_INVALID_CHILD as MAP_GROUP_INVALID_CHILD,
    MAP_GROUP_INVALID_MAP as MAP_GROUP_INVALID_MAP,
    MAP_GROUP_INVALID_MOVE as MAP_GROUP_INVALID_MOVE,
    MAP_GROUP_INVALID_PARENT as MAP_GROUP_INVALID_PARENT,
    MAP_IN_USE as MAP_IN_USE,
    MAXIMUM_USER_PROFILES_USED as MAXIMUM_USER_PROFILES_USED,
    METHOD_FAILED as METHOD_FAILED,
    METHOD_TIMEOUT as METHOD_TIMEOUT,
    NETWORK_NO_ADDRESS_ASSIGNED as NETWORK_NO_ADDRESS_ASSIGNED,
    NO_MORE_STORAGE_SPACE as NO_MORE_STORAGE_SPACE,
    NVRAM_READ_FAIL as NVRAM_READ_FAIL,
    NVRAM_WRITE_FAIL as NVRAM_WRITE_FAIL,
    PASSWORD_LENGTH_EXCEEDED as PASSWORD_LENGTH_EXCEEDED,
    PASSWORD_NOT_CHANGED as PASSWORD_NOT_CHANGED,
    PAYLOAD_DECODING_ERR as PAYLOAD_DECODING_ERR,
    READ_PERMISSION_DENIED as READ_PERMISSION_DENIED,
    ROBOT_IN_EMERGENCY_STOP as ROBOT_IN_EMERGENCY_STOP,
    ROBOT_IN_FAULT as ROBOT_IN_FAULT,
    ROBOT_IN_MAINTENANCE as ROBOT_IN_MAINTENANCE,
    ROBOT_IN_UPDATE_MODE as ROBOT_IN_UPDATE_MODE,
    ROBOT_MOVEMENT_IN_PROGRESS as ROBOT_MOVEMENT_IN_PROGRESS,
    ROBOT_NOT_MOVING as ROBOT_NOT_MOVING,
    ROBOT_NOT_READY as ROBOT_NOT_READY,
    ROUTER_UNVAILABLE as ROUTER_UNVAILABLE,
    SAFETY_THRESHOLD_REACHED as SAFETY_THRESHOLD_REACHED,
    SEND_FAILED as SEND_FAILED,
    SESSION_NOT_IN_CONTROL as SESSION_NOT_IN_CONTROL,
    SINGLE_LEVEL_SERVOING as SINGLE_LEVEL_SERVOING,
    SUB_ERROR_NONE as SUB_ERROR_NONE,
    SubErrorCodes as SubErrorCodes,
    TOO_LARGE_ENCODED_FRAME_BUFFER as TOO_LARGE_ENCODED_FRAME_BUFFER,
    TOO_LARGE_ENCODED_PAYLOAD_BUFFER as TOO_LARGE_ENCODED_PAYLOAD_BUFFER,
    UNIMPLEMENTED as UNIMPLEMENTED,
    UNREGISTERED_FRAME_RECEIVED as UNREGISTERED_FRAME_RECEIVED,
    UNREGISTERED_NOTIFICATION_RECEIVED as UNREGISTERED_NOTIFICATION_RECEIVED,
    UNSUPPORTED_ACTION as UNSUPPORTED_ACTION,
    UNSUPPORTED_BIT_RATE as UNSUPPORTED_BIT_RATE,
    UNSUPPORTED_FOCUS_ACTION as UNSUPPORTED_FOCUS_ACTION,
    UNSUPPORTED_FRAME_RATE as UNSUPPORTED_FRAME_RATE,
    UNSUPPORTED_FRAME_TYPE as UNSUPPORTED_FRAME_TYPE,
    UNSUPPORTED_METHOD as UNSUPPORTED_METHOD,
    UNSUPPORTED_NETWORK_TYPE as UNSUPPORTED_NETWORK_TYPE,
    UNSUPPORTED_OPTION as UNSUPPORTED_OPTION,
    UNSUPPORTED_RESOLUTION as UNSUPPORTED_RESOLUTION,
    UNSUPPORTED_ROBOT_CONFIGURATION as UNSUPPORTED_ROBOT_CONFIGURATION,
    UNSUPPORTED_SERVICE as UNSUPPORTED_SERVICE,
    UPDATE_PERMISSION_DENIED as UPDATE_PERMISSION_DENIED,
    USERNAME_ALREADY_EXISTS as USERNAME_ALREADY_EXISTS,
    USERNAME_EMPTY as USERNAME_EMPTY,
    USERNAME_LENGTH_EXCEEDED as USERNAME_LENGTH_EXCEEDED,
    USER_NOT_FOUND as USER_NOT_FOUND,
    VALUE_IS_ABOVE_MAXIMUM as VALUE_IS_ABOVE_MAXIMUM,
    VALUE_IS_BELOW_MINIMUM as VALUE_IS_BELOW_MINIMUM,
    WIFI_CONNECT_ERROR as WIFI_CONNECT_ERROR,
    WRONG_SERVOING_MODE as WRONG_SERVOING_MODE,
)

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _HeaderVersion:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _HeaderVersionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_HeaderVersion.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESERVED_0: _HeaderVersion.ValueType  # 0
    CURRENT_VERSION: _HeaderVersion.ValueType  # 1
    """Current version"""

class HeaderVersion(_HeaderVersion, metaclass=_HeaderVersionEnumTypeWrapper):
    """Payload Information Bitmask(s):
    FIELDMASK_RESERVED           0xFF000000
    FIELDMASK_PAYLOAD_LENGTH     0x00FFFFFF

    Current version of the header
    """

RESERVED_0: HeaderVersion.ValueType  # 0
CURRENT_VERSION: HeaderVersion.ValueType  # 1
"""Current version"""
global___HeaderVersion = HeaderVersion

class _FrameTypes:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FrameTypesEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FrameTypes.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESERVED: _FrameTypes.ValueType  # 0
    MSG_FRAME_REQUEST: _FrameTypes.ValueType  # 1
    MSG_FRAME_RAW: _FrameTypes.ValueType  # 2
    MSG_FRAME_RESPONSE: _FrameTypes.ValueType  # 3
    MSG_FRAME_NOTIFICATION: _FrameTypes.ValueType  # 5
    MSG_FRAME_PING: _FrameTypes.ValueType  # 7
    MSG_FRAME_PONG: _FrameTypes.ValueType  # 8

class FrameTypes(_FrameTypes, metaclass=_FrameTypesEnumTypeWrapper):
    """Admissible frame types"""

RESERVED: FrameTypes.ValueType  # 0
MSG_FRAME_REQUEST: FrameTypes.ValueType  # 1
MSG_FRAME_RAW: FrameTypes.ValueType  # 2
MSG_FRAME_RESPONSE: FrameTypes.ValueType  # 3
MSG_FRAME_NOTIFICATION: FrameTypes.ValueType  # 5
MSG_FRAME_PING: FrameTypes.ValueType  # 7
MSG_FRAME_PONG: FrameTypes.ValueType  # 8
global___FrameTypes = FrameTypes

class Frame(google.protobuf.message.Message):
    """Defines a Frame format including its header and payload"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADER_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___Header: ...
    payload: builtins.bytes
    def __init__(
        self,
        *,
        header: global___Header | None = ...,
        payload: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header", b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header", b"header", "payload", b"payload"]) -> None: ...

global___Frame = Frame

class Header(google.protobuf.message.Message):
    """Defines the frame header"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRAME_INFO_FIELD_NUMBER: builtins.int
    MESSAGE_INFO_FIELD_NUMBER: builtins.int
    SERVICE_INFO_FIELD_NUMBER: builtins.int
    PAYLOAD_INFO_FIELD_NUMBER: builtins.int
    frame_info: builtins.int
    """Includes frame type, device handle identifier, error code and sub error code"""
    message_info: builtins.int
    """Includes session identifier and message identifier"""
    service_info: builtins.int
    """Includes service version, service identifier and function identifier"""
    payload_info: builtins.int
    """Includes payload length"""
    def __init__(
        self,
        *,
        frame_info: builtins.int = ...,
        message_info: builtins.int = ...,
        service_info: builtins.int = ...,
        payload_info: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["frame_info", b"frame_info", "message_info", b"message_info", "payload_info", b"payload_info", "service_info", b"service_info"]) -> None: ...

global___Header = Header

class Error(google.protobuf.message.Message):
    """Defines an error message"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_CODE_FIELD_NUMBER: builtins.int
    ERROR_SUB_CODE_FIELD_NUMBER: builtins.int
    ERROR_SUB_STRING_FIELD_NUMBER: builtins.int
    error_code: Errors_pb2.ErrorCodes.ValueType
    """Error code. Please refer to Errors.proto for list of error codes"""
    error_sub_code: builtins.int
    """Sub error code. Please refer to Errors.proto for list of sub error codes"""
    error_sub_string: builtins.str
    """For internal usage"""
    def __init__(
        self,
        *,
        error_code: Errors_pb2.ErrorCodes.ValueType = ...,
        error_sub_code: builtins.int = ...,
        error_sub_string: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_code", b"error_code", "error_sub_code", b"error_sub_code", "error_sub_string", b"error_sub_string"]) -> None: ...

global___Error = Error