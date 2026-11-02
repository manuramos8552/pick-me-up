# product.py - Product shown in a slot on the display stand


class Product:
    def __init__(self, productId, name, price, category="", promotion=""):
        self.productId = productId
        self.name = name
        self.price = price
        self.category = category
        self.promotion = promotion
        self.unitsSold = 0

    def getInfo(self):
        """Short text for the LCD: name, price and promotion."""
        info = "{} ${:.2f}".format(self.name, self.price)
        if self.promotion:
            info += " " + self.promotion
        return info
