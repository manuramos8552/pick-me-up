# Pick Me Up - Interactive Store Display

Group 4: Shelf Aware - ISM 6106 System Analysis and Design

IoT display stand built on the Raspberry Pi Pico W. When a customer lifts a
product, a sensor detects it, the slot lights up, the buzzer beeps and the LCD
shows product info. Each pickup is logged, and a password-protected web
dashboard shows managers pickup counts, hold times, items not returned, and lets them refill an empty slot.

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
  - `main.py` - demo loop (being updated to the three-slot stand)
- `docs/` - UML class diagram, proposal, and the design draft materials
  - `software_design.md` - software design section, updated class diagram and slot state diagram (design draft, Nov 2026)

## Still to build
WiFiManager, WebDashboard.

## Running
Copy the files in `src/` to the Pico W with Thonny and run `main.py`.
Never commit Wi-Fi passwords: keep them in a `secrets.py` file that is not uploaded.
