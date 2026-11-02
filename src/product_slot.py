# product_slot.py - One slot on the stand: owns its sensor, light and buzzer
import time
from events import PickupEvent


class ProductSlot:
    def __init__(self, slotId, product, sensor, light, buzzer, display=None):
        self.slotId = slotId
        self.product = product
        self.sensor = sensor
        self.light = light
        self.buzzer = buzzer
        self._display = display      # the stand's shared screen (optional)
        self.isLifted = False
        self.liftTime = 0.0

    def onPickup(self):
        self.isLifted = True
        self.liftTime = time.time()
        self.light.on()
        self.buzzer.beep(150)
        if self._display:
            self._display.showText(self.product.getInfo())

    def onReturn(self):
        self.isLifted = False
        self.light.off()
        if self._display:
            self._display.clear()
        return PickupEvent(self.product, self.liftTime, time.time())

    def checkSensor(self):
        """Call in the main loop. Returns a PickupEvent when the product
        is put back, otherwise None."""
        lifted = self.sensor.isTriggered()
        if lifted and not self.isLifted:
            self.onPickup()
        elif not lifted and self.isLifted:
            return self.onReturn()
        return None
