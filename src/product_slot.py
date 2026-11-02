# product_slot.py - One spot on the display stand: product + sensor + outputs
import time
from events import InteractionEvent


class ProductSlot:
    def __init__(self, slot_id, product, sensor, outputs):
        self._slot_id = slot_id
        self._product = product      # aggregation: product exists on its own
        self._sensor = sensor        # aggregation: sensor hardware
        self._outputs = outputs      # list of OutputDevice
        self._is_lifted = False
        self._lifted_at = 0

    def on_pick_up(self):
        self._is_lifted = True
        self._lifted_at = time.time()
        for device in self._outputs:
            device.activate()

    def on_put_back(self):
        self._is_lifted = False
        for device in self._outputs:
            device.deactivate()
        duration = time.time() - self._lifted_at
        return InteractionEvent(self._product.sku, self._slot_id,
                                self._lifted_at, duration)

    def check_sensor(self):
        """Call in the main loop. Returns an InteractionEvent when a
        pick-up finishes (product put back), otherwise None."""
        triggered = self._sensor.is_triggered()
        if triggered and not self._is_lifted:
            self.on_pick_up()
        elif not triggered and self._is_lifted:
            return self.on_put_back()
        return None
