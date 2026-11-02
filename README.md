# Pick Me Up - Interactive Store Display

Group 4: Shelf Aware - ISM 6106 System Analysis and Design

IoT display stand built on the Raspberry Pi Pico W. When a customer lifts a
product, a sensor detects it, the slot lights up, the buzzer beeps and the LCD
shows product info. Each pickup is logged, and a password-protected web
dashboard shows managers pickup counts, hold times and conversion rates.

## Repository layout
- `src/` - MicroPython classes from the UML object model
  - `store.py` - Store, DisplayStand
  - `product_slot.py` - ProductSlot
  - `product.py` - Product
  - `sensors.py` - Sensor (abstract), IRSensor, LightSensor, WeightSensor
  - `lights.py` - Light, LightStrip
  - `buzzers.py` - Buzzer (abstract), PassiveBuzzer
  - `displays.py` - Display (abstract), LCDDisplay
  - `events.py` - PickupEvent, EventLogger
  - `main.py` - demo loop: one stand, two slots
- `docs/` - UML class diagram and proposal

## Still to build
WiFiManager, WebDashboard.

## Running
Copy the files in `src/` to the Pico W with Thonny and run `main.py`.
Never commit Wi-Fi passwords: keep them in a `secrets.py` file that is not uploaded.
