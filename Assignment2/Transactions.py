from datetime import datetime

class Transactions:
    def __init__(self, barcode, amount):
        self.date = str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
        self.barcode = barcode
        self.amount = int(amount)

    def getDate(self):
        return self.date

    def getBarcode(self):
        return self.barcode

    def getAmount(self):
        return self.amount
