# events.py - PickupEvent and EventLogger
import json
import time

LIKELY_PURCHASE_SECONDS = 120   # not returned within 2 min = likely purchase


class PickupEvent:
    def __init__(self, product, pickupTime, returnTime=None):
        self.product = product
        self.pickupTime = pickupTime
        self.returnTime = returnTime
        self.isReturned = returnTime is not None

    def getHoldSeconds(self):
        end = self.returnTime if self.isReturned else time.time()
        return end - self.pickupTime

    def classify(self):
        if self.isReturned:
            return "returned"            # interest only
        if self.getHoldSeconds() > LIKELY_PURCHASE_SECONDS:
            return "not returned"        # likely purchase
        return "in hand"

    def toDict(self):
        return {"productId": self.product.productId,
                "pickupTime": self.pickupTime,
                "returnTime": self.returnTime,
                "result": self.classify()}


class EventLogger:
    def __init__(self, filename="events.json"):
        self.events = []
        self._filename = filename

    def log(self, event):
        self.events.append(event)
        self.saveToFile()

    def _eventsFor(self, product):
        return [e for e in self.events if e.product.productId == product.productId]

    def getPickupCount(self, product):
        return len(self._eventsFor(product))

    def getAvgHoldTime(self, product):
        events = self._eventsFor(product)
        if not events:
            return 0.0
        return sum(e.getHoldSeconds() for e in events) / len(events)

    def getInterestScore(self, product):
        """Pickups weighted by how long customers hold the product."""
        return self.getPickupCount(product) * (1 + self.getAvgHoldTime(product) / 10)

    def getConversionRate(self, product):
        """Units sold divided by pickups (0 if never picked up)."""
        count = self.getPickupCount(product)
        return product.unitsSold / count if count else 0.0

    def saveToFile(self):
        with open(self._filename, "w") as f:
            json.dump([e.toDict() for e in self.events], f)

    def loadFromFile(self):
        """Returns the saved event records (as dicts) from flash memory."""
        try:
            with open(self._filename) as f:
                return json.load(f)
        except OSError:
            return []
