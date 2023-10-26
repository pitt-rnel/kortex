"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

KINOVA (R) KORTEX (TM)

Copyright (c) 2018 Kinova inc. All rights reserved.

This software may be modified and distributed
under the terms of the BSD 3-Clause license.

Refer to the LICENSE file for details.
"""
from . import Common_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
from .Common_pb2 import (
    ALBANIA_AL as ALBANIA_AL,
    AMERICAN_SAMOA_AS as AMERICAN_SAMOA_AS,
    AMPERE as AMPERE,
    ANGUILLA_AI as ANGUILLA_AI,
    ANTIGUA_AND_BARBUDA_AG as ANTIGUA_AND_BARBUDA_AG,
    ARMSTATE_BASE_INITIALIZATION as ARMSTATE_BASE_INITIALIZATION,
    ARMSTATE_BRAKE_RELEASING as ARMSTATE_BRAKE_RELEASING,
    ARMSTATE_IDLE as ARMSTATE_IDLE,
    ARMSTATE_INITIALIZATION as ARMSTATE_INITIALIZATION,
    ARMSTATE_IN_FAULT as ARMSTATE_IN_FAULT,
    ARMSTATE_MAINTENANCE as ARMSTATE_MAINTENANCE,
    ARMSTATE_RESERVED as ARMSTATE_RESERVED,
    ARMSTATE_SERVOING_LOW_LEVEL as ARMSTATE_SERVOING_LOW_LEVEL,
    ARMSTATE_SERVOING_MANUALLY_CONTROLLED as ARMSTATE_SERVOING_MANUALLY_CONTROLLED,
    ARMSTATE_SERVOING_PLAYING_SEQUENCE as ARMSTATE_SERVOING_PLAYING_SEQUENCE,
    ARMSTATE_SERVOING_READY as ARMSTATE_SERVOING_READY,
    ARMSTATE_UNSPECIFIED as ARMSTATE_UNSPECIFIED,
    ARUBA_AW as ARUBA_AW,
    AUSTRALIA_AU as AUSTRALIA_AU,
    AUSTRIA_AT as AUSTRIA_AT,
    AZERBAIJAN_AZ as AZERBAIJAN_AZ,
    ArmState as ArmState,
    BAHAMAS_BS as BAHAMAS_BS,
    BAHRAIN_BH as BAHRAIN_BH,
    BANGLADESH_BD as BANGLADESH_BD,
    BASE as BASE,
    BELARUS_BY as BELARUS_BY,
    BELGIUM_BE as BELGIUM_BE,
    BERMUDA_BM as BERMUDA_BM,
    BIG_ACTUATOR as BIG_ACTUATOR,
    BOLIVARIAN_REPUBLIC_OF_VENEZUELA_VE as BOLIVARIAN_REPUBLIC_OF_VENEZUELA_VE,
    BOSNIA_AND_HERZEGOVINA_BA as BOSNIA_AND_HERZEGOVINA_BA,
    BRAZIL_BR as BRAZIL_BR,
    BRITISH_VIRGIN_ISLANDS_VG as BRITISH_VIRGIN_ISLANDS_VG,
    BRUNEI_DARUSSALAM_BN as BRUNEI_DARUSSALAM_BN,
    BULGARIA_BG as BULGARIA_BG,
    CAMBODIA_KH as CAMBODIA_KH,
    CANADA_CA as CANADA_CA,
    CARTESIAN_REFERENCE_FRAME_BASE as CARTESIAN_REFERENCE_FRAME_BASE,
    CARTESIAN_REFERENCE_FRAME_MIXED as CARTESIAN_REFERENCE_FRAME_MIXED,
    CARTESIAN_REFERENCE_FRAME_TOOL as CARTESIAN_REFERENCE_FRAME_TOOL,
    CARTESIAN_REFERENCE_FRAME_UNSPECIFIED as CARTESIAN_REFERENCE_FRAME_UNSPECIFIED,
    CAYMAN_ISLANDS_KY as CAYMAN_ISLANDS_KY,
    CELSIUS as CELSIUS,
    CHINA_CN as CHINA_CN,
    COLOMBIA_CO as COLOMBIA_CO,
    COSTA_RICA_CR as COSTA_RICA_CR,
    CROATIA_HR as CROATIA_HR,
    CYPRUS_CY as CYPRUS_CY,
    CZECH_REPUBLIC_CZ as CZECH_REPUBLIC_CZ,
    CartesianReferenceFrame as CartesianReferenceFrame,
    Connection as Connection,
    CountryCode as CountryCode,
    CountryCodeIdentifier as CountryCodeIdentifier,
    DEGREE as DEGREE,
    DEGREE_PER_MILLISECOND as DEGREE_PER_MILLISECOND,
    DEGREE_PER_SECOND as DEGREE_PER_SECOND,
    DEGREE_PER_SECOND_2 as DEGREE_PER_SECOND_2,
    DELETE_PERMISSION as DELETE_PERMISSION,
    DENMARK_DK as DENMARK_DK,
    DeviceHandle as DeviceHandle,
    DeviceTypes as DeviceTypes,
    ECUADOR_EC as ECUADOR_EC,
    EGYPT_EG as EGYPT_EG,
    EL_SALVADOR_SV as EL_SALVADOR_SV,
    ESTONIA_EE as ESTONIA_EE,
    ETHIOPIA_ET as ETHIOPIA_ET,
    Empty as Empty,
    FINLAND_FI as FINLAND_FI,
    FRANCE_FR as FRANCE_FR,
    FRENCH_GUIANA_GF as FRENCH_GUIANA_GF,
    GERMANY_DE as GERMANY_DE,
    GREECE_GR as GREECE_GR,
    GRENADA_GD as GRENADA_GD,
    GRIPPER as GRIPPER,
    GUADELOUPE_GP as GUADELOUPE_GP,
    GUAM_GU as GUAM_GU,
    GUATEMALA_GT as GUATEMALA_GT,
    HOLY_SEE_VATICAN_CITY_STATE_VA as HOLY_SEE_VATICAN_CITY_STATE_VA,
    HONG_KONG_HK as HONG_KONG_HK,
    HUNGARY_HU as HUNGARY_HU,
    ICELAND_IS as ICELAND_IS,
    INDIA_IN as INDIA_IN,
    INDONESIA_ID as INDONESIA_ID,
    INTERCONNECT as INTERCONNECT,
    IRELAND_IE as IRELAND_IE,
    ISRAEL_IL as ISRAEL_IL,
    ITALY_IT as ITALY_IT,
    JAPAN_JP as JAPAN_JP,
    JORDAN_JO as JORDAN_JO,
    KILOGRAM as KILOGRAM,
    KUWAIT_KW as KUWAIT_KW,
    LAO_PDR_LA as LAO_PDR_LA,
    LATVIA_LV as LATVIA_LV,
    LEBANON_LB as LEBANON_LB,
    LESOTHO_LS as LESOTHO_LS,
    LIECHTENSTEIN_LI as LIECHTENSTEIN_LI,
    LITHUANIA_LT as LITHUANIA_LT,
    LUXEMBOURG_LU as LUXEMBOURG_LU,
    MALAWI_MW as MALAWI_MW,
    MALAYSIA_MY as MALAYSIA_MY,
    MALDIVES_MV as MALDIVES_MV,
    MALTA_MT as MALTA_MT,
    MARTINIQUE_MQ as MARTINIQUE_MQ,
    MAURITANIA_MR as MAURITANIA_MR,
    MAURITIUS_MU as MAURITIUS_MU,
    MAYOTTE_YT as MAYOTTE_YT,
    MEDIUM_ACTUATOR as MEDIUM_ACTUATOR,
    METER_PER_SECOND as METER_PER_SECOND,
    METER_PER_SECOND_2 as METER_PER_SECOND_2,
    MEXICO_MX as MEXICO_MX,
    MOLDOVA_MD as MOLDOVA_MD,
    MONACO_MC as MONACO_MC,
    MONGOLIA_MN as MONGOLIA_MN,
    MONTENEGRO_ME as MONTENEGRO_ME,
    MOROCCO_MA as MOROCCO_MA,
    NETHERLANDS_NL as NETHERLANDS_NL,
    NEWTON as NEWTON,
    NEWTON_METER as NEWTON_METER,
    NEW_ZEALAND_NZ as NEW_ZEALAND_NZ,
    NICARAGUA_NI as NICARAGUA_NI,
    NORWAY_NO as NORWAY_NO,
    NOTIFICATION_TYPE_EVENT as NOTIFICATION_TYPE_EVENT,
    NOTIFICATION_TYPE_FIX_RATE as NOTIFICATION_TYPE_FIX_RATE,
    NOTIFICATION_TYPE_THRESHOLD as NOTIFICATION_TYPE_THRESHOLD,
    NOTIFICATION_TYPE_UNSPECIFIED as NOTIFICATION_TYPE_UNSPECIFIED,
    NO_PERMISSION as NO_PERMISSION,
    NotificationHandle as NotificationHandle,
    NotificationOptions as NotificationOptions,
    NotificationType as NotificationType,
    OMAN_OM as OMAN_OM,
    PANAMA_PA as PANAMA_PA,
    PARAGUAY_PY as PARAGUAY_PY,
    PERU_PE as PERU_PE,
    PHILIPPINES_PH as PHILIPPINES_PH,
    POLAND_PL as POLAND_PL,
    PORTUGAL_PT as PORTUGAL_PT,
    PUERTO_RICO_PR as PUERTO_RICO_PR,
    Permission as Permission,
    READ_PERMISSION as READ_PERMISSION,
    REPUBLIC_OF_KOREA_KR as REPUBLIC_OF_KOREA_KR,
    REPUBLIC_OF_MACEDONIA_MK as REPUBLIC_OF_MACEDONIA_MK,
    REUNION_RE as REUNION_RE,
    ROMANIA_RO as ROMANIA_RO,
    RUSSIAN_FEDERATION_RU as RUSSIAN_FEDERATION_RU,
    SAFETY_STATUS_ERROR as SAFETY_STATUS_ERROR,
    SAFETY_STATUS_NORMAL as SAFETY_STATUS_NORMAL,
    SAFETY_STATUS_UNSPECIFIED as SAFETY_STATUS_UNSPECIFIED,
    SAFETY_STATUS_WARNING as SAFETY_STATUS_WARNING,
    SERBIA_RS as SERBIA_RS,
    SINGAPORE_SI as SINGAPORE_SI,
    SLOVAKIA_SK as SLOVAKIA_SK,
    SMALL_ACTUATOR as SMALL_ACTUATOR,
    SOUTH_AFRICA_ZA as SOUTH_AFRICA_ZA,
    SPAIN_ES as SPAIN_ES,
    SRI_LANKA_LK as SRI_LANKA_LK,
    SWEDEN_SE as SWEDEN_SE,
    SWITZERLAND_CH as SWITZERLAND_CH,
    SafetyHandle as SafetyHandle,
    SafetyNotification as SafetyNotification,
    SafetyStatusValue as SafetyStatusValue,
    TAIWAN_PROVINCE_OF_CHINA_TW as TAIWAN_PROVINCE_OF_CHINA_TW,
    THAILAND_TH as THAILAND_TH,
    TICK as TICK,
    TRINIDAD_AND_TOBAGO_TT as TRINIDAD_AND_TOBAGO_TT,
    TUNISIA_TN as TUNISIA_TN,
    TURKEY_TR as TURKEY_TR,
    Timestamp as Timestamp,
    UARTConfiguration as UARTConfiguration,
    UARTDeviceIdentification as UARTDeviceIdentification,
    UARTParity as UARTParity,
    UARTSpeed as UARTSpeed,
    UARTStopBits as UARTStopBits,
    UARTWordLength as UARTWordLength,
    UART_PARITY_EVEN as UART_PARITY_EVEN,
    UART_PARITY_NONE as UART_PARITY_NONE,
    UART_PARITY_ODD as UART_PARITY_ODD,
    UART_PARITY_UNSPECIFIED as UART_PARITY_UNSPECIFIED,
    UART_SPEED_115200 as UART_SPEED_115200,
    UART_SPEED_1382400 as UART_SPEED_1382400,
    UART_SPEED_1612800 as UART_SPEED_1612800,
    UART_SPEED_1843200 as UART_SPEED_1843200,
    UART_SPEED_19200 as UART_SPEED_19200,
    UART_SPEED_2073600 as UART_SPEED_2073600,
    UART_SPEED_2188800 as UART_SPEED_2188800,
    UART_SPEED_2246400 as UART_SPEED_2246400,
    UART_SPEED_230400 as UART_SPEED_230400,
    UART_SPEED_38400 as UART_SPEED_38400,
    UART_SPEED_460800 as UART_SPEED_460800,
    UART_SPEED_4800 as UART_SPEED_4800,
    UART_SPEED_57600 as UART_SPEED_57600,
    UART_SPEED_921600 as UART_SPEED_921600,
    UART_SPEED_9600 as UART_SPEED_9600,
    UART_SPEED_UNSPECIFIED as UART_SPEED_UNSPECIFIED,
    UART_STOP_BITS_0_5 as UART_STOP_BITS_0_5,
    UART_STOP_BITS_1 as UART_STOP_BITS_1,
    UART_STOP_BITS_1_5 as UART_STOP_BITS_1_5,
    UART_STOP_BITS_2 as UART_STOP_BITS_2,
    UART_STOP_BITS_UNSPECIFIED as UART_STOP_BITS_UNSPECIFIED,
    UART_WORD_LENGTH_7 as UART_WORD_LENGTH_7,
    UART_WORD_LENGTH_8 as UART_WORD_LENGTH_8,
    UART_WORD_LENGTH_9 as UART_WORD_LENGTH_9,
    UART_WORD_LENGTH_UNSPECIFIED as UART_WORD_LENGTH_UNSPECIFIED,
    UKRAINE_UA as UKRAINE_UA,
    UNITED_ARAB_EMIRATES_AE as UNITED_ARAB_EMIRATES_AE,
    UNITED_KINGDOM_GB as UNITED_KINGDOM_GB,
    UNITED_STATES_US as UNITED_STATES_US,
    UNSPECIFIED_COUNTRY_CODE as UNSPECIFIED_COUNTRY_CODE,
    UNSPECIFIED_DEVICE_TYPE as UNSPECIFIED_DEVICE_TYPE,
    UNSPECIFIED_UNIT as UNSPECIFIED_UNIT,
    UPDATE_PERMISSION as UPDATE_PERMISSION,
    Unit as Unit,
    UserProfileHandle as UserProfileHandle,
    VIETNAM_VN as VIETNAM_VN,
    VISION as VISION,
    VOLT as VOLT,
    XBIG_ACTUATOR as XBIG_ACTUATOR,
)

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ServiceVersion:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ServiceVersionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ServiceVersion.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESERVED_0: _ServiceVersion.ValueType  # 0
    """Reserved"""
    CURRENT_VERSION: _ServiceVersion.ValueType  # 1
    """Current version"""

class ServiceVersion(_ServiceVersion, metaclass=_ServiceVersionEnumTypeWrapper):
    """Identifies ControlConfig current version"""

RESERVED_0: ServiceVersion.ValueType  # 0
"""Reserved"""
CURRENT_VERSION: ServiceVersion.ValueType  # 1
"""Current version"""
global___ServiceVersion = ServiceVersion

class _ControlConfigurationEvent:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ControlConfigurationEventEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ControlConfigurationEvent.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSPECIFIED_CONTROL_CONFIGURATION_EVENT: _ControlConfigurationEvent.ValueType  # 0
    """Unspecified control configuration event"""
    ANGLE_UNIT_CHANGED: _ControlConfigurationEvent.ValueType  # 1
    """Angle unit changed event"""
    GRAVITY_VECTOR_CHANGED: _ControlConfigurationEvent.ValueType  # 2
    """Gravity vector changed event"""
    JOINT_ADMITTANCE_CONFIGURATION_CHANGED: _ControlConfigurationEvent.ValueType  # 4
    """Joint admittance configuration changed event"""
    NULL_ADMITTANCE_CONFIGURATION_CHANGED: _ControlConfigurationEvent.ValueType  # 5
    """Null admittance configuration changed event"""
    CARTESIAN_ADMITTANCE_CONFIGURATION_CHANGED: _ControlConfigurationEvent.ValueType  # 6
    """Cartesian admittance configuration changed event"""
    JOINT_TORQUE_HYBRID_CONFIGURATION_CHANGED: _ControlConfigurationEvent.ValueType  # 7
    """Joint torque hybrid configuraiton changed event"""
    WRENCH_COMMAND_NORMAL_CONFIGURATION_CHANGED: _ControlConfigurationEvent.ValueType  # 8
    """Wrench commmand normal configuration changed event"""
    WRENCH_COMMAND_RESTRICTED_CONFIGURATION_CHANGED: _ControlConfigurationEvent.ValueType  # 9
    """Wrench command restricted configuration changed event"""
    CONTROL_CONFIGURATION_FACTORY_RESTORED: _ControlConfigurationEvent.ValueType  # 10
    """Control configuration factory restored event"""
    TOOL_CONFIGURATION_CHANGED: _ControlConfigurationEvent.ValueType  # 11
    """Tool configuration event"""
    PAYLOAD_CONFIGURATION_CHANGED: _ControlConfigurationEvent.ValueType  # 12
    """Payload configuration event"""
    CARTESIAN_REFERENCE_CHANGED: _ControlConfigurationEvent.ValueType  # 13
    """Cartesian reference event"""
    CHANGE_CONTROL_MODE_FAILED: _ControlConfigurationEvent.ValueType  # 14
    """Control mode change fail event"""
    JOINT_SPEED_SOFT_LIMITS_CHANGED: _ControlConfigurationEvent.ValueType  # 16
    """Joint speed software limits changed event"""
    TWIST_LINEAR_SOFT_LIMIT_CHANGED: _ControlConfigurationEvent.ValueType  # 17
    """Linear speed software limit changed event"""
    TWIST_ANGULAR_SOFT_LIMIT_CHANGED: _ControlConfigurationEvent.ValueType  # 18
    """Angular speed software limit changed event"""
    JOINT_ACCELERATION_SOFT_LIMITS_CHANGED: _ControlConfigurationEvent.ValueType  # 19
    """Joint acceleration software limits changed event"""
    DESIRED_TWIST_LINEAR_SPEED_CHANGED: _ControlConfigurationEvent.ValueType  # 20
    """Desired joystick twist linear speed changed event"""
    DESIRED_TWIST_ANGULAR_SPEED_CHANGED: _ControlConfigurationEvent.ValueType  # 21
    """Desired joystick twist angular speed changed event"""
    DESIRED_JOINT_SPEED_CHANGED: _ControlConfigurationEvent.ValueType  # 22
    """Desired joystick joint speed changed event"""

class ControlConfigurationEvent(_ControlConfigurationEvent, metaclass=_ControlConfigurationEventEnumTypeWrapper):
    """Admissible control configuration events"""

UNSPECIFIED_CONTROL_CONFIGURATION_EVENT: ControlConfigurationEvent.ValueType  # 0
"""Unspecified control configuration event"""
ANGLE_UNIT_CHANGED: ControlConfigurationEvent.ValueType  # 1
"""Angle unit changed event"""
GRAVITY_VECTOR_CHANGED: ControlConfigurationEvent.ValueType  # 2
"""Gravity vector changed event"""
JOINT_ADMITTANCE_CONFIGURATION_CHANGED: ControlConfigurationEvent.ValueType  # 4
"""Joint admittance configuration changed event"""
NULL_ADMITTANCE_CONFIGURATION_CHANGED: ControlConfigurationEvent.ValueType  # 5
"""Null admittance configuration changed event"""
CARTESIAN_ADMITTANCE_CONFIGURATION_CHANGED: ControlConfigurationEvent.ValueType  # 6
"""Cartesian admittance configuration changed event"""
JOINT_TORQUE_HYBRID_CONFIGURATION_CHANGED: ControlConfigurationEvent.ValueType  # 7
"""Joint torque hybrid configuraiton changed event"""
WRENCH_COMMAND_NORMAL_CONFIGURATION_CHANGED: ControlConfigurationEvent.ValueType  # 8
"""Wrench commmand normal configuration changed event"""
WRENCH_COMMAND_RESTRICTED_CONFIGURATION_CHANGED: ControlConfigurationEvent.ValueType  # 9
"""Wrench command restricted configuration changed event"""
CONTROL_CONFIGURATION_FACTORY_RESTORED: ControlConfigurationEvent.ValueType  # 10
"""Control configuration factory restored event"""
TOOL_CONFIGURATION_CHANGED: ControlConfigurationEvent.ValueType  # 11
"""Tool configuration event"""
PAYLOAD_CONFIGURATION_CHANGED: ControlConfigurationEvent.ValueType  # 12
"""Payload configuration event"""
CARTESIAN_REFERENCE_CHANGED: ControlConfigurationEvent.ValueType  # 13
"""Cartesian reference event"""
CHANGE_CONTROL_MODE_FAILED: ControlConfigurationEvent.ValueType  # 14
"""Control mode change fail event"""
JOINT_SPEED_SOFT_LIMITS_CHANGED: ControlConfigurationEvent.ValueType  # 16
"""Joint speed software limits changed event"""
TWIST_LINEAR_SOFT_LIMIT_CHANGED: ControlConfigurationEvent.ValueType  # 17
"""Linear speed software limit changed event"""
TWIST_ANGULAR_SOFT_LIMIT_CHANGED: ControlConfigurationEvent.ValueType  # 18
"""Angular speed software limit changed event"""
JOINT_ACCELERATION_SOFT_LIMITS_CHANGED: ControlConfigurationEvent.ValueType  # 19
"""Joint acceleration software limits changed event"""
DESIRED_TWIST_LINEAR_SPEED_CHANGED: ControlConfigurationEvent.ValueType  # 20
"""Desired joystick twist linear speed changed event"""
DESIRED_TWIST_ANGULAR_SPEED_CHANGED: ControlConfigurationEvent.ValueType  # 21
"""Desired joystick twist angular speed changed event"""
DESIRED_JOINT_SPEED_CHANGED: ControlConfigurationEvent.ValueType  # 22
"""Desired joystick joint speed changed event"""
global___ControlConfigurationEvent = ControlConfigurationEvent

class _ControlMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ControlModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ControlMode.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSPECIFIED_CONTROL_MODE: _ControlMode.ValueType  # 0
    """Unspecified control mode"""
    ANGULAR_JOYSTICK: _ControlMode.ValueType  # 1
    """Angular joystick mode"""
    CARTESIAN_JOYSTICK: _ControlMode.ValueType  # 2
    """Cartesian joystick mode"""
    ANGULAR_TRAJECTORY: _ControlMode.ValueType  # 4
    """Angular trajectory mode"""
    CARTESIAN_TRAJECTORY: _ControlMode.ValueType  # 5
    """Cartesian trajectory mode"""
    CARTESIAN_ADMITTANCE: _ControlMode.ValueType  # 6
    """Cartesian admittance mode"""
    JOINT_ADMITTANCE: _ControlMode.ValueType  # 7
    """Joint admittance mode"""
    NULL_SPACE_ADMITTANCE: _ControlMode.ValueType  # 8
    """Null space mode"""
    FORCE_CONTROL: _ControlMode.ValueType  # 10
    """Force control mode"""
    FORCE_CONTROL_MOTION_RESTRICTED: _ControlMode.ValueType  # 11
    """Force control motion restricted mode"""
    CARTESIAN_WAYPOINT_TRAJECTORY: _ControlMode.ValueType  # 12
    """Cartesian waypoint trajectory mode"""
    IDLE: _ControlMode.ValueType  # 13
    """Idle"""

class ControlMode(_ControlMode, metaclass=_ControlModeEnumTypeWrapper):
    """Admissible robot control modes"""

UNSPECIFIED_CONTROL_MODE: ControlMode.ValueType  # 0
"""Unspecified control mode"""
ANGULAR_JOYSTICK: ControlMode.ValueType  # 1
"""Angular joystick mode"""
CARTESIAN_JOYSTICK: ControlMode.ValueType  # 2
"""Cartesian joystick mode"""
ANGULAR_TRAJECTORY: ControlMode.ValueType  # 4
"""Angular trajectory mode"""
CARTESIAN_TRAJECTORY: ControlMode.ValueType  # 5
"""Cartesian trajectory mode"""
CARTESIAN_ADMITTANCE: ControlMode.ValueType  # 6
"""Cartesian admittance mode"""
JOINT_ADMITTANCE: ControlMode.ValueType  # 7
"""Joint admittance mode"""
NULL_SPACE_ADMITTANCE: ControlMode.ValueType  # 8
"""Null space mode"""
FORCE_CONTROL: ControlMode.ValueType  # 10
"""Force control mode"""
FORCE_CONTROL_MOTION_RESTRICTED: ControlMode.ValueType  # 11
"""Force control motion restricted mode"""
CARTESIAN_WAYPOINT_TRAJECTORY: ControlMode.ValueType  # 12
"""Cartesian waypoint trajectory mode"""
IDLE: ControlMode.ValueType  # 13
"""Idle"""
global___ControlMode = ControlMode

class GravityVector(google.protobuf.message.Message):
    """Defines the gravity vector in terms of the robot base frame. If not explicitly configured, it defaults to (0, 0, -9.81), assuming a mounting on a horizontal surface. If the robot is mounted on a wall or ceiling, the gravity vector relative to the base frame will change. The control library needs to be aware of this to accurately compensate for gravity."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.float
    """x (meters / second^squared)"""
    y: builtins.float
    """y (meters / second^squared)"""
    z: builtins.float
    """z (meters / second^squared)"""
    def __init__(
        self,
        *,
        x: builtins.float = ...,
        y: builtins.float = ...,
        z: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___GravityVector = GravityVector

class Position(google.protobuf.message.Message):
    """A Cartesian position"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.float
    """x position (in meters)"""
    y: builtins.float
    """y position (in meters)"""
    z: builtins.float
    """z position (in meters)"""
    def __init__(
        self,
        *,
        x: builtins.float = ...,
        y: builtins.float = ...,
        z: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Position = Position

class PayloadInformation(google.protobuf.message.Message):
    """Defines payload information"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAYLOAD_MASS_FIELD_NUMBER: builtins.int
    PAYLOAD_MASS_CENTER_FIELD_NUMBER: builtins.int
    payload_mass: builtins.float
    """Tool mass in kg"""
    @property
    def payload_mass_center(self) -> global___Position:
        """Tool mass center position relative to the tool reference frame"""
    def __init__(
        self,
        *,
        payload_mass: builtins.float = ...,
        payload_mass_center: global___Position | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["payload_mass_center", b"payload_mass_center"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["payload_mass", b"payload_mass", "payload_mass_center", b"payload_mass_center"]) -> None: ...

global___PayloadInformation = PayloadInformation

class CartesianTransform(google.protobuf.message.Message):
    """Defines a Cartesian transform"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    THETA_X_FIELD_NUMBER: builtins.int
    THETA_Y_FIELD_NUMBER: builtins.int
    THETA_Z_FIELD_NUMBER: builtins.int
    x: builtins.float
    """x (in meters)"""
    y: builtins.float
    """y (in meters)"""
    z: builtins.float
    """z (in meters)"""
    theta_x: builtins.float
    """Theta x (in degrees)"""
    theta_y: builtins.float
    """Theta y (in degrees)"""
    theta_z: builtins.float
    """Theta z (in degrees)"""
    def __init__(
        self,
        *,
        x: builtins.float = ...,
        y: builtins.float = ...,
        z: builtins.float = ...,
        theta_x: builtins.float = ...,
        theta_y: builtins.float = ...,
        theta_z: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["theta_x", b"theta_x", "theta_y", b"theta_y", "theta_z", b"theta_z", "x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___CartesianTransform = CartesianTransform

class ToolConfiguration(google.protobuf.message.Message):
    """Defines a tool configuration"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOOL_TRANSFORM_FIELD_NUMBER: builtins.int
    TOOL_MASS_FIELD_NUMBER: builtins.int
    TOOL_MASS_CENTER_FIELD_NUMBER: builtins.int
    @property
    def tool_transform(self) -> global___CartesianTransform:
        """Cartesian transform tool"""
    tool_mass: builtins.float
    """Tool mass (in kg)"""
    @property
    def tool_mass_center(self) -> global___Position:
        """Tool mass center position relative to the interface module reference frame"""
    def __init__(
        self,
        *,
        tool_transform: global___CartesianTransform | None = ...,
        tool_mass: builtins.float = ...,
        tool_mass_center: global___Position | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tool_mass_center", b"tool_mass_center", "tool_transform", b"tool_transform"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tool_mass", b"tool_mass", "tool_mass_center", b"tool_mass_center", "tool_transform", b"tool_transform"]) -> None: ...

global___ToolConfiguration = ToolConfiguration

class ControlConfigurationNotification(google.protobuf.message.Message):
    """Notification about a single control configuration event"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EVENT_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    USER_HANDLE_FIELD_NUMBER: builtins.int
    CONNECTION_FIELD_NUMBER: builtins.int
    event: global___ControlConfigurationEvent.ValueType
    @property
    def timestamp(self) -> Common_pb2.Timestamp:
        """Event timestamp"""
    @property
    def user_handle(self) -> Common_pb2.UserProfileHandle:
        """User that caused the factory event to occur"""
    @property
    def connection(self) -> Common_pb2.Connection:
        """Connection that caused the configuration event"""
    def __init__(
        self,
        *,
        event: global___ControlConfigurationEvent.ValueType = ...,
        timestamp: Common_pb2.Timestamp | None = ...,
        user_handle: Common_pb2.UserProfileHandle | None = ...,
        connection: Common_pb2.Connection | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connection", b"connection", "timestamp", b"timestamp", "user_handle", b"user_handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connection", b"connection", "event", b"event", "timestamp", b"timestamp", "user_handle", b"user_handle"]) -> None: ...

global___ControlConfigurationNotification = ControlConfigurationNotification

class CartesianReferenceFrameInfo(google.protobuf.message.Message):
    """Cartesian reference frame"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REFERENCE_FRAME_FIELD_NUMBER: builtins.int
    reference_frame: Common_pb2.CartesianReferenceFrame.ValueType
    """Reference frame"""
    def __init__(
        self,
        *,
        reference_frame: Common_pb2.CartesianReferenceFrame.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["reference_frame", b"reference_frame"]) -> None: ...

global___CartesianReferenceFrameInfo = CartesianReferenceFrameInfo

class TwistLinearSoftLimit(google.protobuf.message.Message):
    """Software twist linear speed limit"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTROL_MODE_FIELD_NUMBER: builtins.int
    TWIST_LINEAR_SOFT_LIMIT_FIELD_NUMBER: builtins.int
    control_mode: global___ControlMode.ValueType
    """Control mode"""
    twist_linear_soft_limit: builtins.float
    """Software linear twist limit"""
    def __init__(
        self,
        *,
        control_mode: global___ControlMode.ValueType = ...,
        twist_linear_soft_limit: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["control_mode", b"control_mode", "twist_linear_soft_limit", b"twist_linear_soft_limit"]) -> None: ...

global___TwistLinearSoftLimit = TwistLinearSoftLimit

class TwistAngularSoftLimit(google.protobuf.message.Message):
    """Software twist angular speed limit"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTROL_MODE_FIELD_NUMBER: builtins.int
    TWIST_ANGULAR_SOFT_LIMIT_FIELD_NUMBER: builtins.int
    control_mode: global___ControlMode.ValueType
    """Control mode"""
    twist_angular_soft_limit: builtins.float
    """Software angular twist limit"""
    def __init__(
        self,
        *,
        control_mode: global___ControlMode.ValueType = ...,
        twist_angular_soft_limit: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["control_mode", b"control_mode", "twist_angular_soft_limit", b"twist_angular_soft_limit"]) -> None: ...

global___TwistAngularSoftLimit = TwistAngularSoftLimit

class JointSpeedSoftLimits(google.protobuf.message.Message):
    """Software joint speed limits"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTROL_MODE_FIELD_NUMBER: builtins.int
    JOINT_SPEED_SOFT_LIMITS_FIELD_NUMBER: builtins.int
    control_mode: global___ControlMode.ValueType
    """Control mode"""
    @property
    def joint_speed_soft_limits(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Software joint speed limits"""
    def __init__(
        self,
        *,
        control_mode: global___ControlMode.ValueType = ...,
        joint_speed_soft_limits: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["control_mode", b"control_mode", "joint_speed_soft_limits", b"joint_speed_soft_limits"]) -> None: ...

global___JointSpeedSoftLimits = JointSpeedSoftLimits

class JointAccelerationSoftLimits(google.protobuf.message.Message):
    """Software Joint acceleration limits"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTROL_MODE_FIELD_NUMBER: builtins.int
    JOINT_ACCELERATION_SOFT_LIMITS_FIELD_NUMBER: builtins.int
    control_mode: global___ControlMode.ValueType
    """Control mode"""
    @property
    def joint_acceleration_soft_limits(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Software acceleration limits"""
    def __init__(
        self,
        *,
        control_mode: global___ControlMode.ValueType = ...,
        joint_acceleration_soft_limits: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["control_mode", b"control_mode", "joint_acceleration_soft_limits", b"joint_acceleration_soft_limits"]) -> None: ...

global___JointAccelerationSoftLimits = JointAccelerationSoftLimits

class KinematicLimits(google.protobuf.message.Message):
    """Kinematic limits"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTROL_MODE_FIELD_NUMBER: builtins.int
    TWIST_LINEAR_FIELD_NUMBER: builtins.int
    TWIST_ANGULAR_FIELD_NUMBER: builtins.int
    JOINT_SPEED_LIMITS_FIELD_NUMBER: builtins.int
    JOINT_ACCELERATION_LIMITS_FIELD_NUMBER: builtins.int
    control_mode: global___ControlMode.ValueType
    """Control mode"""
    twist_linear: builtins.float
    """Linear twist limits"""
    twist_angular: builtins.float
    """Angular twist limits"""
    @property
    def joint_speed_limits(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Joint speed limits"""
    @property
    def joint_acceleration_limits(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Joint Acceleration limits"""
    def __init__(
        self,
        *,
        control_mode: global___ControlMode.ValueType = ...,
        twist_linear: builtins.float = ...,
        twist_angular: builtins.float = ...,
        joint_speed_limits: collections.abc.Iterable[builtins.float] | None = ...,
        joint_acceleration_limits: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["control_mode", b"control_mode", "joint_acceleration_limits", b"joint_acceleration_limits", "joint_speed_limits", b"joint_speed_limits", "twist_angular", b"twist_angular", "twist_linear", b"twist_linear"]) -> None: ...

global___KinematicLimits = KinematicLimits

class KinematicLimitsList(google.protobuf.message.Message):
    """Kinematic limits"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KINEMATIC_LIMITS_LIST_FIELD_NUMBER: builtins.int
    @property
    def kinematic_limits_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KinematicLimits]:
        """List of kinematic limits"""
    def __init__(
        self,
        *,
        kinematic_limits_list: collections.abc.Iterable[global___KinematicLimits] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["kinematic_limits_list", b"kinematic_limits_list"]) -> None: ...

global___KinematicLimitsList = KinematicLimitsList

class DesiredSpeeds(google.protobuf.message.Message):
    """Desired Joystick speeds."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LINEAR_FIELD_NUMBER: builtins.int
    ANGULAR_FIELD_NUMBER: builtins.int
    JOINT_SPEED_FIELD_NUMBER: builtins.int
    linear: builtins.float
    """Desired linear speed (meters / second)"""
    angular: builtins.float
    """Desired angular speed (degrees / second)"""
    @property
    def joint_speed(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Desired joint speeds (degrees / second)"""
    def __init__(
        self,
        *,
        linear: builtins.float = ...,
        angular: builtins.float = ...,
        joint_speed: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["angular", b"angular", "joint_speed", b"joint_speed", "linear", b"linear"]) -> None: ...

global___DesiredSpeeds = DesiredSpeeds

class LinearTwist(google.protobuf.message.Message):
    """Desired Joystick linear speed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LINEAR_FIELD_NUMBER: builtins.int
    linear: builtins.float
    """Desired linear speed (meters / second)"""
    def __init__(
        self,
        *,
        linear: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["linear", b"linear"]) -> None: ...

global___LinearTwist = LinearTwist

class AngularTwist(google.protobuf.message.Message):
    """Desired Joystick angular speed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ANGULAR_FIELD_NUMBER: builtins.int
    angular: builtins.float
    """Desired angular speed (degrees / second)"""
    def __init__(
        self,
        *,
        angular: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["angular", b"angular"]) -> None: ...

global___AngularTwist = AngularTwist

class JointSpeeds(google.protobuf.message.Message):
    """Desired Joystick joint speeds."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOINT_SPEED_FIELD_NUMBER: builtins.int
    @property
    def joint_speed(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Desired joint speeds (degrees / second)"""
    def __init__(
        self,
        *,
        joint_speed: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["joint_speed", b"joint_speed"]) -> None: ...

global___JointSpeeds = JointSpeeds

class ControlModeInformation(google.protobuf.message.Message):
    """Control mode information"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTROL_MODE_FIELD_NUMBER: builtins.int
    control_mode: global___ControlMode.ValueType
    """Control mode"""
    def __init__(
        self,
        *,
        control_mode: global___ControlMode.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["control_mode", b"control_mode"]) -> None: ...

global___ControlModeInformation = ControlModeInformation

class ControlModeNotification(google.protobuf.message.Message):
    """Notification about a single control mode event"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTROL_MODE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    USER_HANDLE_FIELD_NUMBER: builtins.int
    CONNECTION_FIELD_NUMBER: builtins.int
    control_mode: global___ControlMode.ValueType
    """New control mode"""
    @property
    def timestamp(self) -> Common_pb2.Timestamp:
        """Event timestamp"""
    @property
    def user_handle(self) -> Common_pb2.UserProfileHandle:
        """User that caused the control mode event"""
    @property
    def connection(self) -> Common_pb2.Connection:
        """Connection that caused the control mode event"""
    def __init__(
        self,
        *,
        control_mode: global___ControlMode.ValueType = ...,
        timestamp: Common_pb2.Timestamp | None = ...,
        user_handle: Common_pb2.UserProfileHandle | None = ...,
        connection: Common_pb2.Connection | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connection", b"connection", "timestamp", b"timestamp", "user_handle", b"user_handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connection", b"connection", "control_mode", b"control_mode", "timestamp", b"timestamp", "user_handle", b"user_handle"]) -> None: ...

global___ControlModeNotification = ControlModeNotification
