# lights.py - Light and LightStrip (NeoPixel)
import time
from machine import Pin
import neopixel


class Light:
    """Single LED."""

    def __init__(self, pin):
        self.pin = pin
        self._led = Pin(pin, Pin.OUT)

    def on(self):
        self._led.on()

    def off(self):
        self._led.off()

    def blink(self, times):
        for _ in range(times):
            self.on()
            time.sleep(0.2)
            self.off()
            time.sleep(0.2)


class LightStrip(Light):
    """NeoPixel strip that lights up the slot that was picked up."""

    def __init__(self, pin, numPixels, color=(0, 150, 255)):
        self.pin = pin
        self.numPixels = numPixels
        self._color = color
        self._np = neopixel.NeoPixel(Pin(pin), numPixels)

    def setColor(self, color):
        self._color = color
        for i in range(self.numPixels):
            self._np[i] = color
        self._np.write()

    def on(self):
        self.setColor(self._color)

    def off(self):
        for i in range(self.numPixels):
            self._np[i] = (0, 0, 0)
        self._np.write()
