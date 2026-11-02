# main.py - Demo: one stand with two product slots
import time
from product import Product
from sensors import LightSensor, IRSensor
from lights import Light
from buzzers import PassiveBuzzer
from product_slot import ProductSlot
from store import Store, DisplayStand
from events import EventLogger

store = Store("Demo Store")
stand = DisplayStand(1, "Aisle 3")      # add an LCDDisplay here when wired
store.addStand(stand)

earbuds = Product(1, "Earbuds", 49.99, "Audio", "10% off")
charger = Product(2, "Charger", 19.99, "Accessories")

buzzer = PassiveBuzzer(14)
stand.addSlot(ProductSlot(1, earbuds, LightSensor(26), Light(15), buzzer, stand.screen))
stand.addSlot(ProductSlot(2, charger, IRSensor(16), Light(13), buzzer, stand.screen))

logger = EventLogger()

while True:
    for event in stand.checkSlots():
        logger.log(event)
        p = event.product
        print(p.name, "held", round(event.getHoldSeconds(), 1), "s |",
              "pickups:", logger.getPickupCount(p),
              "avg hold:", round(logger.getAvgHoldTime(p), 1), "s")
    time.sleep(0.1)
