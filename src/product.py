# product.py - Product sitting on a display stand
class Product:
    def __init__(self, sku, name, price, description=""):
        self._sku = sku
        self._name = name
        self._price = price
        self._description = description

    @property
    def sku(self):
        return self._sku

    def get_info(self):
        return "{} - ${:.2f}\n{}".format(self._name, self._price, self._description)
