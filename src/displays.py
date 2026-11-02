# displays.py - Display (abstract) and LCDDisplay


class Display:
    """Abstract parent class for screens."""

    def showText(self, text):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError


class LCDDisplay(Display):
    """I2C character LCD (e.g. 16x2). `lcd` is the driver object from the
    lab's LCD library (e.g. I2cLcd), so this class works with our lab code."""

    def __init__(self, lcd, rows=2, cols=16):
        self._lcd = lcd
        self.rows = rows
        self.cols = cols

    def showText(self, text):
        self._lcd.clear()
        self._lcd.putstr(text[: self.rows * self.cols])

    def clear(self):
        self._lcd.clear()
