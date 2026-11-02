# sensors.py - Sensor (abstract) and its subclasses
# isTriggered() returns True when the product has been LIFTED off the slot.
from machine import ADC, Pin


class Sensor:
    """Abstract parent class for all sensors."""

    def __init__(self, pin):
        self.pin = pin

    def read(self):
        raise NotImplementedError("Subclasses must implement read()")

    def isTriggered(self):
        raise NotImplementedError("Subclasses must implement isTriggered()")


class IRSensor(Sensor):
    """IR obstacle sensor under the product. Output is LOW (0) while
    the product is in front of it, HIGH (1) when the product is lifted."""

    def __init__(self, pin):
        super().__init__(pin)
        self._input = Pin(pin, Pin.IN)

    def read(self):
        return self._input.value()

    def isTriggered(self):
        return self.read() == 1


class LightSensor(Sensor):
    """Photoresistor (LDR) under the product. Covered = dark.
    When the product is lifted, light rises past the threshold."""

    def __init__(self, pin, threshold=30000):
        super().__init__(pin)
        self.threshold = threshold
        self._adc = ADC(Pin(pin))

    def read(self):
        return self._adc.read_u16()

    def isTriggered(self):
        return self.read() > self.threshold


class WeightSensor(Sensor):
    """Stretch feature: load cell with an HX711 amplifier.
    Detects a lift (weight drops) and, later, a different product put back."""

    def __init__(self, pin, hx711, emptyWeight=5):
        super().__init__(pin)
        self._hx711 = hx711          # driver object from the HX711 library
        self.emptyWeight = emptyWeight

    def read(self):
        return self._hx711.get_units()

    def isTriggered(self):
        return self.read() < self.emptyWeight
