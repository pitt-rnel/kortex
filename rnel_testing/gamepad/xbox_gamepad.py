""" This module requires  the inputs library (https://github.com/zeth/inputs).
However, we bypass all the event simulation and just use it to grab the state of the 
xbox gamepad whenever the user requests it. This eliminates the need for background threads
and more complicated async configurations for simple testing.

pip install inputs

or 

git clone https://github.com/zeth/inputs.git
cd inputs
python setup.py install

"""

import math
import time
import ctypes

from typing import Optional, NamedTuple, Tuple
from inputs import (
    devices,
    XinputState,
    XINPUT_ERROR_SUCCESS,
    XINPUT_ERROR_DEVICE_NOT_CONNECTED,
)


def get_bit(value, bitnum) -> int:
    return (value >> bitnum) & 1


class JoystickValue(NamedTuple):
    x: float
    y: float


class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self._state_names = (
            "buttons",
            "l_thumb_x",
            "l_thumb_y",
            "left_trigger",
            "r_thumb_x",
            "r_thumb_y",
            "right_trigger",
        )

        self.names = (
            "left_joystick",
            "right_joystick",
            "left_trigger",
            "right_trigger",
            "up",
            "down",
            "left",
            "right",
            "menu",
            "view",
            "left_thumb",
            "right_thumb",
            "left_bumper",
            "right_bumper",
            "A",
            "B",
            "X",
            "Y",
        )

        self.buttons_bitmap = dict(
            up=0,
            down=1,
            left=2,
            right=3,
            menu=4,
            view=5,
            left_thumb=6,
            right_thumb=7,
            left_bumper=8,
            right_bumper=9,
            A=12,
            B=13,
            X=14,
            Y=15,
        )

        self.gamepad = devices.gamepads[0]

    def read_controller(self) -> Optional[XinputState]:
        """Read the state of the gamepad."""
        state = XinputState()

        res = self.gamepad.manager.xinput.XInputGetState(
            self.gamepad._GamePad__device_number, ctypes.byref(state)
        )

        if res == XINPUT_ERROR_SUCCESS:
            return state
        if res != XINPUT_ERROR_DEVICE_NOT_CONNECTED:
            raise RuntimeError(
                "Unknown error %d attempting to get state of device %d"
                % (res, self.gamepad._GamePad__device_number)
            )
        return None

    def read(self):
        state = self.read_controller()
        if state is not None:
            self.state = state.gamepad
            return {n: getattr(self, n) for n in self.names}

    @property
    def left_joystick(self) -> Tuple[float, float]:
        return JoystickValue(
            self.state.l_thumb_x / XboxController.MAX_JOY_VAL,
            self.state.l_thumb_y / XboxController.MAX_JOY_VAL,
        )

    @property
    def right_joystick(self) -> Tuple[float, float]:
        return JoystickValue(
            self.state.r_thumb_x / XboxController.MAX_JOY_VAL,
            self.state.r_thumb_y / XboxController.MAX_JOY_VAL,
        )

    @property
    def right_trigger(self) -> float:
        return self.state.right_trigger / XboxController.MAX_TRIG_VAL

    @property
    def left_trigger(self) -> float:
        return self.state.left_trigger / XboxController.MAX_TRIG_VAL

    @property
    def up(self) -> int:
        return get_bit(self.state.buttons, 0)

    @property
    def down(self) -> int:
        return get_bit(self.state.buttons, 1)

    @property
    def left(self) -> int:
        return get_bit(self.state.buttons, 2)

    @property
    def right(self) -> int:
        return get_bit(self.state.buttons, 3)

    @property
    def menu(self) -> int:
        return get_bit(self.state.buttons, 4)

    @property
    def view(self) -> int:
        return get_bit(self.state.buttons, 5)

    @property
    def left_thumb(self) -> int:
        return get_bit(self.state.buttons, 6)

    @property
    def right_thumb(self) -> int:
        return get_bit(self.state.buttons, 7)

    @property
    def left_bumper(self) -> int:
        return get_bit(self.state.buttons, 8)

    @property
    def right_bumper(self) -> int:
        return get_bit(self.state.buttons, 9)

    @property
    def A(self) -> int:
        return get_bit(self.state.buttons, 12)

    @property
    def B(self) -> int:
        return get_bit(self.state.buttons, 13)

    @property
    def X(self) -> int:
        return get_bit(self.state.buttons, 14)

    @property
    def Y(self) -> int:
        return get_bit(self.state.buttons, 15)


if __name__ == "__main__":
    joy = XboxController()
    while True:
        values = str(joy.read()).replace("\n", " ")
        print(f"\r{values}", end="")
        time.sleep(0.050)
