# sensors.py - Sensor base class and subclasses (MicroPython, Raspberry Pi Pico W)
from machine import ADC, Pin


class Sensor:
    """Abstract sensor. Subclasses must implement read()."""

    def __init__(self, pin, threshold):
        self._pin = pin
        self._threshold = threshold

    def read(self):
        raise NotImplementedError("Subclasses must implement read()")

    def is_triggered(self):
        """True when the product has been lifted off the slot."""
        return self.read() > self._threshold


class LightSensor(Sensor):
    """Photoresistor under the product: more light = product lifted."""

    def __init__(self, pin, threshold=30000):
        super().__init__(pin, threshold)
        self._adc = ADC(Pin(pin))

    def read(self):
        return self._adc.read_u16()

    def calibrate(self, samples=10):
        """Set the threshold just above the 'product resting' light level."""
        base = sum(self.read() for _ in range(samples)) // samples
        self._threshold = base + 5000


class ButtonSensor(Sensor):
    """Push button pressed down by the product's weight."""

    def __init__(self, pin, pull_up=True):
        super().__init__(pin, threshold=0)
        self._pull_up = pull_up
        self._btn = Pin(pin, Pin.IN, Pin.PULL_UP if pull_up else Pin.PULL_DOWN)

    def read(self):
        # Pull-up: pressed (product present) reads 0, released (lifted) reads 1
        value = self._btn.value()
        return value if self._pull_up else 1 - value
