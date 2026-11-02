# Pick Me Up - Interactive Store Display

IoT display stand built on the Raspberry Pi Pico W. When a customer lifts a
product, a sensor detects it, the stand lights up / beeps / shows product info,
and the event is logged. A Wi-Fi web dashboard shows the store manager which
products get picked up versus which ones actually sell.

## Repository layout
- `src/` - MicroPython classes from the object model
  - `product.py` - Product
  - `sensors.py` - Sensor (abstract), LightSensor, ButtonSensor
  - `outputs.py` - OutputDevice (abstract), LED, Buzzer
  - `events.py` - InteractionEvent, EventLogger
  - `product_slot.py` - ProductSlot
  - `main.py` - demo loop for one slot
- `docs/` - UML class diagram (PDF/PNG) and proposal

## Still to build
Store, DisplayStand, OLEDScreen, WiFiManager, WebDashboard, InterestReport,
SalesRecord, User / StoreManager / Admin, AuthService.

## Running
Copy the files in `src/` to the Pico W with Thonny and run `main.py`.
