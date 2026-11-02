# outputs.py - Output devices that react when a product is picked up
import time
from machine import Pin, PWM


class OutputDevice:
    """Abstract output device."""

    def __init__(self, pin):
        self._pin = pin
        self._enabled = True

    def activate(self):
        raise NotImplementedError

    def deactivate(self):
        raise NotImplementedError


class LED(OutputDevice):
    def __init__(self, pin):
        super().__init__(pin)
        self._led = Pin(pin, Pin.OUT)

    def activate(self):
        if self._enabled:
            self._led.on()

    def deactivate(self):
        self._led.off()

    def blink(self, times=3, delay=0.2):
        for _ in range(times):
            self.activate()
            time.sleep(delay)
            self.deactivate()
            time.sleep(delay)


class Buzzer(OutputDevice):
    def __init__(self, pin, tone=1000):
        super().__init__(pin)
        self._tone = tone
        self._pwm = PWM(Pin(pin))

    def activate(self):
        if self._enabled:
            self._pwm.freq(self._tone)
            self._pwm.duty_u16(32768)

    def deactivate(self):
        self._pwm.duty_u16(0)

    def beep(self, duration_ms=150):
        self.activate()
        time.sleep_ms(duration_ms)
        self.deactivate()
