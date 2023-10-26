"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

KINOVA (R) KORTEX (TM)

Copyright (c) 2018 Kinova inc. All rights reserved.

This software may be modified and distributed
under the terms of the BSD 3-Clause license.

Refer to the LICENSE file for details.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
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

class MessageId(google.protobuf.message.Message):
    """Message identifier for command or feedback"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDENTIFIER_FIELD_NUMBER: builtins.int
    identifier: builtins.int
    """Message ID (first 2 bytes : device ID, last 2 bytes : sequence number)"""
    def __init__(
        self,
        *,
        identifier: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["identifier", b"identifier"]) -> None: ...

global___MessageId = MessageId

class MotorCommand(google.protobuf.message.Message):
    """Command to a single gripper motor"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MOTOR_ID_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    VELOCITY_FIELD_NUMBER: builtins.int
    FORCE_FIELD_NUMBER: builtins.int
    motor_id: builtins.int
    """Motor ID (1, nb_motor)"""
    position: builtins.float
    """Desired position of the gripper fingers in percentage (0-100%)"""
    velocity: builtins.float
    """Desired velocity in percentage (0-100%) with which position will be set"""
    force: builtins.float
    """This field is deprecated and unused. It will be removed in a future release."""
    def __init__(
        self,
        *,
        motor_id: builtins.int = ...,
        position: builtins.float = ...,
        velocity: builtins.float = ...,
        force: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["force", b"force", "motor_id", b"motor_id", "position", b"position", "velocity", b"velocity"]) -> None: ...

global___MotorCommand = MotorCommand

class Command(google.protobuf.message.Message):
    """Command sent to a gripper"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMAND_ID_FIELD_NUMBER: builtins.int
    FLAGS_FIELD_NUMBER: builtins.int
    MOTOR_CMD_FIELD_NUMBER: builtins.int
    @property
    def command_id(self) -> global___MessageId:
        """MessageId"""
    flags: builtins.int
    """Flags"""
    @property
    def motor_cmd(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MotorCommand]:
        """Array of finger commands, one for each finger of the gripper."""
    def __init__(
        self,
        *,
        command_id: global___MessageId | None = ...,
        flags: builtins.int = ...,
        motor_cmd: collections.abc.Iterable[global___MotorCommand] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["command_id", b"command_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["command_id", b"command_id", "flags", b"flags", "motor_cmd", b"motor_cmd"]) -> None: ...

global___Command = Command

class MotorFeedback(google.protobuf.message.Message):
    """Status feedback from a single gripper motor"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MOTOR_ID_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    VELOCITY_FIELD_NUMBER: builtins.int
    CURRENT_MOTOR_FIELD_NUMBER: builtins.int
    VOLTAGE_FIELD_NUMBER: builtins.int
    TEMPERATURE_MOTOR_FIELD_NUMBER: builtins.int
    motor_id: builtins.int
    """Motor ID (1, nb_motor)"""
    position: builtins.float
    """Position of the gripper fingers in percentage (0-100%)"""
    velocity: builtins.float
    """Velocity of the gripper fingers in percentage (0-100%)"""
    current_motor: builtins.float
    """Current comsumed by the gripper motor (mA)"""
    voltage: builtins.float
    """Motor Voltage (V)"""
    temperature_motor: builtins.float
    """Motor temperature. (degrees Celsius)"""
    def __init__(
        self,
        *,
        motor_id: builtins.int = ...,
        position: builtins.float = ...,
        velocity: builtins.float = ...,
        current_motor: builtins.float = ...,
        voltage: builtins.float = ...,
        temperature_motor: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["current_motor", b"current_motor", "motor_id", b"motor_id", "position", b"position", "temperature_motor", b"temperature_motor", "velocity", b"velocity", "voltage", b"voltage"]) -> None: ...

global___MotorFeedback = MotorFeedback

class Feedback(google.protobuf.message.Message):
    """Status feedback from a gripper"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEEDBACK_ID_FIELD_NUMBER: builtins.int
    STATUS_FLAGS_FIELD_NUMBER: builtins.int
    FAULT_BANK_A_FIELD_NUMBER: builtins.int
    FAULT_BANK_B_FIELD_NUMBER: builtins.int
    WARNING_BANK_A_FIELD_NUMBER: builtins.int
    WARNING_BANK_B_FIELD_NUMBER: builtins.int
    MOTOR_FIELD_NUMBER: builtins.int
    @property
    def feedback_id(self) -> global___MessageId:
        """MessageId"""
    status_flags: builtins.int
    """Status flags (see GripperConfig.RobotiqGripperStatusFlags)"""
    fault_bank_a: builtins.int
    """Fault bank A (see GripperConfig.SafetyIdentifier)"""
    fault_bank_b: builtins.int
    """Fault bank B (see GripperConfig.SafetyIdentifier)"""
    warning_bank_a: builtins.int
    """Warning bank A (see GripperConfig.SafetyIdentifier)"""
    warning_bank_b: builtins.int
    """Warning bank B (see GripperConfig.SafetyIdentifier)"""
    @property
    def motor(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MotorFeedback]: ...
    def __init__(
        self,
        *,
        feedback_id: global___MessageId | None = ...,
        status_flags: builtins.int = ...,
        fault_bank_a: builtins.int = ...,
        fault_bank_b: builtins.int = ...,
        warning_bank_a: builtins.int = ...,
        warning_bank_b: builtins.int = ...,
        motor: collections.abc.Iterable[global___MotorFeedback] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["feedback_id", b"feedback_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fault_bank_a", b"fault_bank_a", "fault_bank_b", b"fault_bank_b", "feedback_id", b"feedback_id", "motor", b"motor", "status_flags", b"status_flags", "warning_bank_a", b"warning_bank_a", "warning_bank_b", b"warning_bank_b"]) -> None: ...

global___Feedback = Feedback

class CustomDataUnit(google.protobuf.message.Message):
    """Custom data"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

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
    def ClearField(self, field_name: typing_extensions.Literal["custom_data_0", b"custom_data_0", "custom_data_1", b"custom_data_1", "custom_data_10", b"custom_data_10", "custom_data_11", b"custom_data_11", "custom_data_12", b"custom_data_12", "custom_data_13", b"custom_data_13", "custom_data_14", b"custom_data_14", "custom_data_15", b"custom_data_15", "custom_data_2", b"custom_data_2", "custom_data_3", b"custom_data_3", "custom_data_4", b"custom_data_4", "custom_data_5", b"custom_data_5", "custom_data_6", b"custom_data_6", "custom_data_7", b"custom_data_7", "custom_data_8", b"custom_data_8", "custom_data_9", b"custom_data_9"]) -> None: ...

global___CustomDataUnit = CustomDataUnit

class CustomData(google.protobuf.message.Message):
    """Custom data from gripper and gripper motors"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CUSTOM_DATA_ID_FIELD_NUMBER: builtins.int
    GRIPPER_CUSTOM_DATA_FIELD_NUMBER: builtins.int
    MOTOR_CUSTOM_DATA_FIELD_NUMBER: builtins.int
    @property
    def custom_data_id(self) -> global___MessageId:
        """MessageId"""
    @property
    def gripper_custom_data(self) -> global___CustomDataUnit: ...
    @property
    def motor_custom_data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CustomDataUnit]: ...
    def __init__(
        self,
        *,
        custom_data_id: global___MessageId | None = ...,
        gripper_custom_data: global___CustomDataUnit | None = ...,
        motor_custom_data: collections.abc.Iterable[global___CustomDataUnit] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["custom_data_id", b"custom_data_id", "gripper_custom_data", b"gripper_custom_data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["custom_data_id", b"custom_data_id", "gripper_custom_data", b"gripper_custom_data", "motor_custom_data", b"motor_custom_data"]) -> None: ...

global___CustomData = CustomData
