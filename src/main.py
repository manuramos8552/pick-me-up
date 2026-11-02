# main.py - Demo loop: one slot with a light sensor, LED and buzzer
import time
from product import Product
from sensors import LightSensor
from outputs import LED, Buzzer
from product_slot import ProductSlot
from events import EventLogger

product = Product("SKU-001", "Wireless Earbuds", 49.99, "Bluetooth 5.3, 24h battery")
sensor = LightSensor(pin=26)
sensor.calibrate()
slot = ProductSlot("A1", product, sensor, [LED(15), Buzzer(14)])
logger = EventLogger()

while True:
    event = slot.check_sensor()
    if event:
        logger.log(event)
        print("Logged:", event.to_dict())
        print("Totals:", logger.count_by_sku())
    time.sleep(0.1)
