class Product:
    def __init__(self, barcode, name, desc, price):
        self.barcode = barcode
        self.name = name
        self.desc = desc
        self.price = price

    # def __str__(self):
    # return f"{self.barcode} {self.name} {self.desc} {self.price}"

    def print_Details(self):
        return f"{self.name}, {self.desc}, {self.price}"

    def __eq__(self, other_product):
        if self.barcode == other_product.barcode:
            return True
        else:
            return False

    def getBarcode(self):
        return self.barcode

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def getPrice(self):
        return self.price