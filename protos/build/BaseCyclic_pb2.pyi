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
import .InterconnectCyclicMessage_pb2
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
from .InterconnectCyclicMessage_pb2 import (
    Command as Command,
    CustomData as CustomData,
    Feedback as Feedback,
    MessageId as MessageId,
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
    """Identifies BaseCyclic current version"""

RESERVED_0: ServiceVersion.ValueType  # 0
"""Reserved"""
CURRENT_VERSION: ServiceVersion.ValueType  # 1
"""Current version"""
global___ServiceVersion = ServiceVersion

class ActuatorCommand(google.protobuf.message.Message):
    """Defines an actuator command"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMAND_ID_FIELD_NUMBER: builtins.int
    FLAGS_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    VELOCITY_FIELD_NUMBER: builtins.int
    TORQUE_JOINT_FIELD_NUMBER: builtins.int
    CURRENT_MOTOR_FIELD_NUMBER: builtins.int
    command_id: builtins.int
    """Command ID (first 2 bytes: device ID, last 2 bytes: sequence number)"""
    flags: builtins.int
    """Flags"""
    position: builtins.float
    """Desired position of the actuator (in degrees)"""
    velocity: builtins.float
    """Desired velocity of the actuator (in degrees per second)"""
    torque_joint: builtins.float
    """Desired torque of the actuator (in Newton * meters)"""
    current_motor: builtins.float
    """Desired current of the motor (in Amperes)"""
    def __init__(
        self,
        *,
        command_id: builtins.int = ...,
        flags: builtins.int = ...,
        position: builtins.float = ...,
        velocity: builtins.float = ...,
        torque_joint: builtins.float = ...,
        current_motor: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["command_id", b"command_id", "current_motor", b"current_motor", "flags", b"flags", "position", b"position", "torque_joint", b"torque_joint", "velocity", b"velocity"]) -> None: ...

global___ActuatorCommand = ActuatorCommand

class ActuatorFeedback(google.protobuf.message.Message):
    """Defines the feedback provided by an actuator"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMAND_ID_FIELD_NUMBER: builtins.int
    STATUS_FLAGS_FIELD_NUMBER: builtins.int
    JITTER_COMM_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    VELOCITY_FIELD_NUMBER: builtins.int
    TORQUE_FIELD_NUMBER: builtins.int
    CURRENT_MOTOR_FIELD_NUMBER: builtins.int
    VOLTAGE_FIELD_NUMBER: builtins.int
    TEMPERATURE_MOTOR_FIELD_NUMBER: builtins.int
    TEMPERATURE_CORE_FIELD_NUMBER: builtins.int
    FAULT_BANK_A_FIELD_NUMBER: builtins.int
    FAULT_BANK_B_FIELD_NUMBER: builtins.int
    WARNING_BANK_A_FIELD_NUMBER: builtins.int
    WARNING_BANK_B_FIELD_NUMBER: builtins.int
    command_id: builtins.int
    """Command ID (first 2 bytes: device ID, last 2 bytes: sequence number)"""
    status_flags: builtins.int
    """Status flags"""
    jitter_comm: builtins.int
    """Jitter from the communication (in microseconds)"""
    position: builtins.float
    """Position of the actuator (in degrees)"""
    velocity: builtins.float
    """Velocity of the actuator (in degrees per second)"""
    torque: builtins.float
    """Torque of the actuator (in Newton * meters)"""
    current_motor: builtins.float
    """Current of the motor (in Amperes)"""
    voltage: builtins.float
    """Voltage of the main board (in Volts)"""
    temperature_motor: builtins.float
    """Motor temperature (maximum of the three (3) phase temperatures in °C)"""
    temperature_core: builtins.float
    """Microcontroller temperature (in degrees Celsius)"""
    fault_bank_a: builtins.int
    """Fault bank A"""
    fault_bank_b: builtins.int
    """Fault bank B"""
    warning_bank_a: builtins.int
    """Warning bank A"""
    warning_bank_b: builtins.int
    """Warning bank B"""
    def __init__(
        self,
        *,
        command_id: builtins.int = ...,
        status_flags: builtins.int = ...,
        jitter_comm: builtins.int = ...,
        position: builtins.float = ...,
        velocity: builtins.float = ...,
        torque: builtins.float = ...,
        current_motor: builtins.float = ...,
        voltage: builtins.float = ...,
        temperature_motor: builtins.float = ...,
        temperature_core: builtins.float = ...,
        fault_bank_a: builtins.int = ...,
        fault_bank_b: builtins.int = ...,
        warning_bank_a: builtins.int = ...,
        warning_bank_b: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["command_id", b"command_id", "current_motor", b"current_motor", "fault_bank_a", b"fault_bank_a", "fault_bank_b", b"fault_bank_b", "jitter_comm", b"jitter_comm", "position", b"position", "status_flags", b"status_flags", "temperature_core", b"temperature_core", "temperature_motor", b"temperature_motor", "torque", b"torque", "velocity", b"velocity", "voltage", b"voltage", "warning_bank_a", b"warning_bank_a", "warning_bank_b", b"warning_bank_b"]) -> None: ...

global___ActuatorFeedback = ActuatorFeedback

class ActuatorCustomData(google.protobuf.message.Message):
    """Custom development data from an actuator, content varies according to debug needs"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMAND_ID_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_0_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_1_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_2_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_3_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_4_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_5_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_6_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_7_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_8_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_9_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_10_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_11_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_12_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_13_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_14_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_15_FIELD_NUMBER: builtins.int
    command_id: builtins.int
    """Command ID (first 2 bytes: device ID, last 2 bytes: sequence number)"""
    custom_data_0: builtins.int
    """Custom data word 0"""
    custom_data_1: builtins.int
    """Custom data word 1"""
    custom_data_2: builtins.int
    """Custom data word 2"""
    custom_data_3: builtins.int
    """Custom data word 3"""
    custom_data_4: builtins.int
    """Custom data word 4"""
    custom_data_5: builtins.int
    """Custom data word 5"""
    custom_data_6: builtins.int
    """Custom data word 6"""
    custom_data_7: builtins.int
    """Custom data word 7"""
    custom_data_8: builtins.int
    """Custom data word 8"""
    custom_data_9: builtins.int
    """Custom data word 9"""
    custom_data_10: builtins.int
    """Custom data word 10"""
    custom_data_11: builtins.int
    """Custom data word 11"""
    custom_data_12: builtins.int
    """Custom data word 12"""
    custom_data_13: builtins.int
    """Custom data word 13"""
    custom_data_14: builtins.int
    """Custom data word 14"""
    custom_data_15: builtins.int
    """Custom data word 15"""
    def __init__(
        self,
        *,
        command_id: builtins.int = ...,
        custom_data_0: builtins.int = ...,
        custom_data_1: builtins.int = ...,
        custom_data_2: builtins.int = ...,
        custom_data_3: builtins.int = ...,
        custom_data_4: builtins.int = ...,
        custom_data_5: builtins.int = ...,
        custom_data_6: builtins.int = ...,
        custom_data_7: builtins.int = ...,
        custom_data_8: builtins.int = ...,
        custom_data_9: builtins.int = ...,
        custom_data_10: builtins.int = ...,
        custom_data_11: builtins.int = ...,
        custom_data_12: builtins.int = ...,
        custom_data_13: builtins.int = ...,
        custom_data_14: builtins.int = ...,
        custom_data_15: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["command_id", b"command_id", "custom_data_0", b"custom_data_0", "custom_data_1", b"custom_data_1", "custom_data_10", b"custom_data_10", "custom_data_11", b"custom_data_11", "custom_data_12", b"custom_data_12", "custom_data_13", b"custom_data_13", "custom_data_14", b"custom_data_14", "custom_data_15", b"custom_data_15", "custom_data_2", b"custom_data_2", "custom_data_3", b"custom_data_3", "custom_data_4", b"custom_data_4", "custom_data_5", b"custom_data_5", "custom_data_6", b"custom_data_6", "custom_data_7", b"custom_data_7", "custom_data_8", b"custom_data_8", "custom_data_9", b"custom_data_9"]) -> None: ...

global___ActuatorCustomData = ActuatorCustomData

class BaseFeedback(google.protobuf.message.Message):
    """Defines the feedback provided by the base"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTIVE_STATE_CONNECTION_IDENTIFIER_FIELD_NUMBER: builtins.int
    ACTIVE_STATE_FIELD_NUMBER: builtins.int
    ARM_VOLTAGE_FIELD_NUMBER: builtins.int
    ARM_CURRENT_FIELD_NUMBER: builtins.int
    TEMPERATURE_CPU_FIELD_NUMBER: builtins.int
    TEMPERATURE_AMBIENT_FIELD_NUMBER: builtins.int
    IMU_ACCELERATION_X_FIELD_NUMBER: builtins.int
    IMU_ACCELERATION_Y_FIELD_NUMBER: builtins.int
    IMU_ACCELERATION_Z_FIELD_NUMBER: builtins.int
    IMU_ANGULAR_VELOCITY_X_FIELD_NUMBER: builtins.int
    IMU_ANGULAR_VELOCITY_Y_FIELD_NUMBER: builtins.int
    IMU_ANGULAR_VELOCITY_Z_FIELD_NUMBER: builtins.int
    TOOL_POSE_X_FIELD_NUMBER: builtins.int
    TOOL_POSE_Y_FIELD_NUMBER: builtins.int
    TOOL_POSE_Z_FIELD_NUMBER: builtins.int
    TOOL_POSE_THETA_X_FIELD_NUMBER: builtins.int
    TOOL_POSE_THETA_Y_FIELD_NUMBER: builtins.int
    TOOL_POSE_THETA_Z_FIELD_NUMBER: builtins.int
    TOOL_TWIST_LINEAR_X_FIELD_NUMBER: builtins.int
    TOOL_TWIST_LINEAR_Y_FIELD_NUMBER: builtins.int
    TOOL_TWIST_LINEAR_Z_FIELD_NUMBER: builtins.int
    TOOL_TWIST_ANGULAR_X_FIELD_NUMBER: builtins.int
    TOOL_TWIST_ANGULAR_Y_FIELD_NUMBER: builtins.int
    TOOL_TWIST_ANGULAR_Z_FIELD_NUMBER: builtins.int
    TOOL_EXTERNAL_WRENCH_FORCE_X_FIELD_NUMBER: builtins.int
    TOOL_EXTERNAL_WRENCH_FORCE_Y_FIELD_NUMBER: builtins.int
    TOOL_EXTERNAL_WRENCH_FORCE_Z_FIELD_NUMBER: builtins.int
    TOOL_EXTERNAL_WRENCH_TORQUE_X_FIELD_NUMBER: builtins.int
    TOOL_EXTERNAL_WRENCH_TORQUE_Y_FIELD_NUMBER: builtins.int
    TOOL_EXTERNAL_WRENCH_TORQUE_Z_FIELD_NUMBER: builtins.int
    FAULT_BANK_A_FIELD_NUMBER: builtins.int
    FAULT_BANK_B_FIELD_NUMBER: builtins.int
    WARNING_BANK_A_FIELD_NUMBER: builtins.int
    WARNING_BANK_B_FIELD_NUMBER: builtins.int
    COMMANDED_TOOL_POSE_X_FIELD_NUMBER: builtins.int
    COMMANDED_TOOL_POSE_Y_FIELD_NUMBER: builtins.int
    COMMANDED_TOOL_POSE_Z_FIELD_NUMBER: builtins.int
    COMMANDED_TOOL_POSE_THETA_X_FIELD_NUMBER: builtins.int
    COMMANDED_TOOL_POSE_THETA_Y_FIELD_NUMBER: builtins.int
    COMMANDED_TOOL_POSE_THETA_Z_FIELD_NUMBER: builtins.int
    active_state_connection_identifier: builtins.int
    """Connection identifier of the last processed command which triggered an arm state change"""
    active_state: Common_pb2.ArmState.ValueType
    """Active state of the arm"""
    arm_voltage: builtins.float
    """Arm voltage (in Volts)"""
    arm_current: builtins.float
    """Arm current (in Amperes)"""
    temperature_cpu: builtins.float
    """CPU temperature (in degree Celsius)"""
    temperature_ambient: builtins.float
    """Ambient temperature (in degree Celsius)"""
    imu_acceleration_x: builtins.float
    """IMU Measured acceleration (X-Axis) of the base (in meters per second squared)"""
    imu_acceleration_y: builtins.float
    """IMU Measured acceleration (Y-Axis) of the base (in meters per second squared)"""
    imu_acceleration_z: builtins.float
    """IMU Measured acceleration (Z-Axis) of the base (in meters per second squared)"""
    imu_angular_velocity_x: builtins.float
    """IMU Measured angular velocity (X-Axis) of the base (in degrees per second)"""
    imu_angular_velocity_y: builtins.float
    """IMU Measured angular velocity (Y-Axis) of the base (in degrees per second)"""
    imu_angular_velocity_z: builtins.float
    """IMU Measured angular velocity (Z-Axis) of the base (in degrees per second)"""
    tool_pose_x: builtins.float
    """Measured Cartesian position (X-Axis) of the tool (in meters)"""
    tool_pose_y: builtins.float
    """Measured Cartesian position (Y-Axis) of the tool (in meters)"""
    tool_pose_z: builtins.float
    """Measured Cartesian position (Z-Axis) of the tool (in meters)"""
    tool_pose_theta_x: builtins.float
    """Measured Cartesian orientation (X-Axis) of the tool (in degrees)"""
    tool_pose_theta_y: builtins.float
    """Measured Cartesian orientation (Y-Axis) of the tool (in degrees)"""
    tool_pose_theta_z: builtins.float
    """Measured Cartesian orientation (Z-Axis) of the tool (in degrees)"""
    tool_twist_linear_x: builtins.float
    """Measured Cartesian linear velocity (X-Axis) of the tool (in meters per second)"""
    tool_twist_linear_y: builtins.float
    """Measured Cartesian linear velocity (Y-Axis) of the tool (in meters per second)"""
    tool_twist_linear_z: builtins.float
    """Measured Cartesian linear velocity (Z-Axis) of the tool (in meters per second)"""
    tool_twist_angular_x: builtins.float
    """Measured Cartesian angular velocity (X-Axis) of the tool (in degrees per second)"""
    tool_twist_angular_y: builtins.float
    """Measured Cartesian angular velocity (Y-Axis) of the tool (in degrees per second)"""
    tool_twist_angular_z: builtins.float
    """Measured Cartesian angular velocity (Z-Axis) of the tool (in degrees per second)"""
    tool_external_wrench_force_x: builtins.float
    """Computed force in X-Axis from external wrench (in Newton)"""
    tool_external_wrench_force_y: builtins.float
    """Computed force in Y-Axis from external wrench (in Newton)"""
    tool_external_wrench_force_z: builtins.float
    """Computed force in Z-Axis from external wrench (in Newton)"""
    tool_external_wrench_torque_x: builtins.float
    """Computed torque about X-axis from external wrench (in Newton-meters)"""
    tool_external_wrench_torque_y: builtins.float
    """Computed torque about Y-axis from external wrench (in Newton-meters)"""
    tool_external_wrench_torque_z: builtins.float
    """Computed torque about Z-axis from external wrench (in Newton-meters)"""
    fault_bank_a: builtins.int
    """The arm fault flags bank A (0 if no fault) see Base.SafetyIdentifier"""
    fault_bank_b: builtins.int
    """The arm fault flags bank B (0 if no fault) see Base.SafetyIdentifier"""
    warning_bank_a: builtins.int
    """The arm warning flags bank A (0 if no warning) see Base.SafetyIdentifier"""
    warning_bank_b: builtins.int
    """The arm warning flags bank B (0 if no warning) see Base.SafetyIdentifier"""
    commanded_tool_pose_x: builtins.float
    """Commanded Cartesian position (X-Axis) of the tool (in meters)"""
    commanded_tool_pose_y: builtins.float
    """Commanded Cartesian position (Y-Axis) of the tool (in meters)"""
    commanded_tool_pose_z: builtins.float
    """Commanded Cartesian position (Z-Axis) of the tool (in meters)"""
    commanded_tool_pose_theta_x: builtins.float
    """Commanded Cartesian orientation (X-Axis) of the tool (in degrees)"""
    commanded_tool_pose_theta_y: builtins.float
    """Commanded Cartesian orientation (Y-Axis) of the tool (in degrees)"""
    commanded_tool_pose_theta_z: builtins.float
    """Commanded Cartesian orientation (Z-Axis) of the tool (in degrees)"""
    def __init__(
        self,
        *,
        active_state_connection_identifier: builtins.int = ...,
        active_state: Common_pb2.ArmState.ValueType = ...,
        arm_voltage: builtins.float = ...,
        arm_current: builtins.float = ...,
        temperature_cpu: builtins.float = ...,
        temperature_ambient: builtins.float = ...,
        imu_acceleration_x: builtins.float = ...,
        imu_acceleration_y: builtins.float = ...,
        imu_acceleration_z: builtins.float = ...,
        imu_angular_velocity_x: builtins.float = ...,
        imu_angular_velocity_y: builtins.float = ...,
        imu_angular_velocity_z: builtins.float = ...,
        tool_pose_x: builtins.float = ...,
        tool_pose_y: builtins.float = ...,
        tool_pose_z: builtins.float = ...,
        tool_pose_theta_x: builtins.float = ...,
        tool_pose_theta_y: builtins.float = ...,
        tool_pose_theta_z: builtins.float = ...,
        tool_twist_linear_x: builtins.float = ...,
        tool_twist_linear_y: builtins.float = ...,
        tool_twist_linear_z: builtins.float = ...,
        tool_twist_angular_x: builtins.float = ...,
        tool_twist_angular_y: builtins.float = ...,
        tool_twist_angular_z: builtins.float = ...,
        tool_external_wrench_force_x: builtins.float = ...,
        tool_external_wrench_force_y: builtins.float = ...,
        tool_external_wrench_force_z: builtins.float = ...,
        tool_external_wrench_torque_x: builtins.float = ...,
        tool_external_wrench_torque_y: builtins.float = ...,
        tool_external_wrench_torque_z: builtins.float = ...,
        fault_bank_a: builtins.int = ...,
        fault_bank_b: builtins.int = ...,
        warning_bank_a: builtins.int = ...,
        warning_bank_b: builtins.int = ...,
        commanded_tool_pose_x: builtins.float = ...,
        commanded_tool_pose_y: builtins.float = ...,
        commanded_tool_pose_z: builtins.float = ...,
        commanded_tool_pose_theta_x: builtins.float = ...,
        commanded_tool_pose_theta_y: builtins.float = ...,
        commanded_tool_pose_theta_z: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_state", b"active_state", "active_state_connection_identifier", b"active_state_connection_identifier", "arm_current", b"arm_current", "arm_voltage", b"arm_voltage", "commanded_tool_pose_theta_x", b"commanded_tool_pose_theta_x", "commanded_tool_pose_theta_y", b"commanded_tool_pose_theta_y", "commanded_tool_pose_theta_z", b"commanded_tool_pose_theta_z", "commanded_tool_pose_x", b"commanded_tool_pose_x", "commanded_tool_pose_y", b"commanded_tool_pose_y", "commanded_tool_pose_z", b"commanded_tool_pose_z", "fault_bank_a", b"fault_bank_a", "fault_bank_b", b"fault_bank_b", "imu_acceleration_x", b"imu_acceleration_x", "imu_acceleration_y", b"imu_acceleration_y", "imu_acceleration_z", b"imu_acceleration_z", "imu_angular_velocity_x", b"imu_angular_velocity_x", "imu_angular_velocity_y", b"imu_angular_velocity_y", "imu_angular_velocity_z", b"imu_angular_velocity_z", "temperature_ambient", b"temperature_ambient", "temperature_cpu", b"temperature_cpu", "tool_external_wrench_force_x", b"tool_external_wrench_force_x", "tool_external_wrench_force_y", b"tool_external_wrench_force_y", "tool_external_wrench_force_z", b"tool_external_wrench_force_z", "tool_external_wrench_torque_x", b"tool_external_wrench_torque_x", "tool_external_wrench_torque_y", b"tool_external_wrench_torque_y", "tool_external_wrench_torque_z", b"tool_external_wrench_torque_z", "tool_pose_theta_x", b"tool_pose_theta_x", "tool_pose_theta_y", b"tool_pose_theta_y", "tool_pose_theta_z", b"tool_pose_theta_z", "tool_pose_x", b"tool_pose_x", "tool_pose_y", b"tool_pose_y", "tool_pose_z", b"tool_pose_z", "tool_twist_angular_x", b"tool_twist_angular_x", "tool_twist_angular_y", b"tool_twist_angular_y", "tool_twist_angular_z", b"tool_twist_angular_z", "tool_twist_linear_x", b"tool_twist_linear_x", "tool_twist_linear_y", b"tool_twist_linear_y", "tool_twist_linear_z", b"tool_twist_linear_z", "warning_bank_a", b"warning_bank_a", "warning_bank_b", b"warning_bank_b"]) -> None: ...

global___BaseFeedback = BaseFeedback

class CustomData(google.protobuf.message.Message):
    """Custom development data, content varies according to debug needs"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRAME_ID_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_0_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_1_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_2_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_3_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_4_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_5_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_6_FIELD_NUMBER: builtins.int
    CUSTOM_DATA_7_FIELD_NUMBER: builtins.int
    ACTUATORS_CUSTOM_DATA_FIELD_NUMBER: builtins.int
    INTERCONNECT_CUSTOM_DATA_FIELD_NUMBER: builtins.int
    frame_id: builtins.int
    """Frame ID"""
    custom_data_0: builtins.int
    """Custom data word 0"""
    custom_data_1: builtins.int
    """Custom data word 1"""
    custom_data_2: builtins.int
    """Custom data word 2"""
    custom_data_3: builtins.int
    """Custom data word 3"""
    custom_data_4: builtins.int
    """Custom data word 4"""
    custom_data_5: builtins.int
    """Custom data word 5"""
    custom_data_6: builtins.int
    """Custom data word 6"""
    custom_data_7: builtins.int
    """Custom data word 7"""
    @property
    def actuators_custom_data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ActuatorCustomData]:
        """Actuator custom data (repeated)"""
    @property
    def interconnect_custom_data(self) -> InterconnectCyclicMessage_pb2.CustomData:
        """Interconnect custom data"""
    def __init__(
        self,
        *,
        frame_id: builtins.int = ...,
        custom_data_0: builtins.int = ...,
        custom_data_1: builtins.int = ...,
        custom_data_2: builtins.int = ...,
        custom_data_3: builtins.int = ...,
        custom_data_4: builtins.int = ...,
        custom_data_5: builtins.int = ...,
        custom_data_6: builtins.int = ...,
        custom_data_7: builtins.int = ...,
        actuators_custom_data: collections.abc.Iterable[global___ActuatorCustomData] | None = ...,
        interconnect_custom_data: InterconnectCyclicMessage_pb2.CustomData | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["interconnect_custom_data", b"interconnect_custom_data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actuators_custom_data", b"actuators_custom_data", "custom_data_0", b"custom_data_0", "custom_data_1", b"custom_data_1", "custom_data_2", b"custom_data_2", "custom_data_3", b"custom_data_3", "custom_data_4", b"custom_data_4", "custom_data_5", b"custom_data_5", "custom_data_6", b"custom_data_6", "custom_data_7", b"custom_data_7", "frame_id", b"frame_id", "interconnect_custom_data", b"interconnect_custom_data"]) -> None: ...

global___CustomData = CustomData

class Command(google.protobuf.message.Message):
    """Defines a command provided to robot devices (actuators and interface)"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRAME_ID_FIELD_NUMBER: builtins.int
    ACTUATORS_FIELD_NUMBER: builtins.int
    INTERCONNECT_FIELD_NUMBER: builtins.int
    frame_id: builtins.int
    """Frame ID"""
    @property
    def actuators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ActuatorCommand]:
        """Actuator command (repeated)"""
    @property
    def interconnect(self) -> InterconnectCyclicMessage_pb2.Command:
        """Interface command"""
    def __init__(
        self,
        *,
        frame_id: builtins.int = ...,
        actuators: collections.abc.Iterable[global___ActuatorCommand] | None = ...,
        interconnect: InterconnectCyclicMessage_pb2.Command | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["interconnect", b"interconnect"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actuators", b"actuators", "frame_id", b"frame_id", "interconnect", b"interconnect"]) -> None: ...

global___Command = Command

class Feedback(google.protobuf.message.Message):
    """Defines the feedback provided by robot devices (base, actuators and interface)"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRAME_ID_FIELD_NUMBER: builtins.int
    BASE_FIELD_NUMBER: builtins.int
    ACTUATORS_FIELD_NUMBER: builtins.int
    INTERCONNECT_FIELD_NUMBER: builtins.int
    frame_id: builtins.int
    """Frame ID"""
    @property
    def base(self) -> global___BaseFeedback:
        """Base feedback"""
    @property
    def actuators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ActuatorFeedback]:
        """Actuator feedback"""
    @property
    def interconnect(self) -> InterconnectCyclicMessage_pb2.Feedback:
        """Interface feedback"""
    def __init__(
        self,
        *,
        frame_id: builtins.int = ...,
        base: global___BaseFeedback | None = ...,
        actuators: collections.abc.Iterable[global___ActuatorFeedback] | None = ...,
        interconnect: InterconnectCyclicMessage_pb2.Feedback | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base", b"base", "interconnect", b"interconnect"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actuators", b"actuators", "base", b"base", "frame_id", b"frame_id", "interconnect", b"interconnect"]) -> None: ...

global___Feedback = Feedback
