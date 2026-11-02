# buzzers.py - Buzzer (abstract) and PassiveBuzzer
import time
from machine import Pin, PWM


class Buzzer:
    """Abstract parent class for sound devices."""

    def __init__(self, pin):
        self.pin = pin

    def play(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError


class PassiveBuzzer(Buzzer):
    """Passive buzzer driven with PWM so it can play a tone."""

    def __init__(self, pin, tone=1000):
        super().__init__(pin)
        self.tone = tone
        self._pwm = PWM(Pin(pin))
        self._pwm.duty_u16(0)

    def play(self):
        self._pwm.freq(self.tone)
        self._pwm.duty_u16(32768)

    def stop(self):
        self._pwm.duty_u16(0)

    def beep(self, duration):
        """Beep for `duration` milliseconds."""
        self.play()
        time.sleep_ms(duration)
        self.stop()
