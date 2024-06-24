import sqlite3
import openpyxl
from openpyxl.chart import LineChart, BarChart, Reference
from datetime import datetime


class SupermarketDAO:
    def __init__(self, db_name='supermarket.db'):
        try:
            self.db = sqlite3.connect(db_name)
            self.cursor = self.db.cursor()
            self.initDB()
        except Exception as e:
            return print("SupermarketDAO : Database Connect Error!!")
        # create a connection to the database

    def connectDB(self, db_name='supermarket.db'):
        try:
            self.db = sqlite3.connect(db_name)
            self.cursor = self.db.cursor()
        except Exception as e:
            return print("SupermarketDAO : Database Connect Error!!")

    def initDB(self):
        # Initialize Database
        try:
            # Create Users Table
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Users (Username text primary key unique, Password text)")
            self.cursor.execute("INSERT OR IGNORE INTO Users VALUES('admin', '123123')")
            self.disconnect()
            self.connectDB()
            # Create Foods, Transactions Table
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Foods (barcode text primary key unique,name,desc,price)")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Transactions (date,barcode,amount)")
            # Insert Data into the Foods table
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('111','Milk','2litre','30' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('112','Bread','500g','30' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('113','Blueberry','1BB','30' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('114', 'Cranberry','1CB','20' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('115', 'Carrot','1ca', '24' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('116', 'Cleaning Tool Set','CTS','40' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('117', 'WaterMelon','WM' ,'10' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('118', 'Grape','Gpe','10' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('119', 'Apple','1','10' )")
            self.cursor.execute("INSERT OR IGNORE INTO Foods VALUES ('120', 'Sausage','1K','10' )")

            self.cursor.commit()
            # Check Product
            for x in self.cursor.execute("SELECT* FROM Foods"):
                print(x)
        except Exception as e:
            return print("Database Initialize is Done")

    def addProductToDB(self, product):
        try:
            self.cursor.execute(
                f"INSERT INTO Foods VALUES ('{product.barcode}','{product.name}','{product.desc}',{product.price})")
            self.db.commit()
            return True
        except Exception as e:
            print("SupermarketDAO : Add Food Error!!\nPlease Check Query or Connection")
            return False

    def listAllProducts(self):
        try:
            self.connectDB()
            res_products = self.cursor.execute('SELECT * FROM Foods').fetchall()
            for i in range(0, len(res_products)):
                for j in range(0, len(res_products) - 1):
                    if res_products[j][0] > res_products[j + 1][0]:
                        temp = res_products[j]
                        res_products[j] = res_products[j + 1]
                        res_products[j + 1] = temp
            for res in res_products:
                print(res)
            return res_products
        except Exception as e:
            return print("SupermarketDAO : List All Food Error!!\nPlease Check Cursor or Connection")

    def findProduct(self, barcode):
        try:
            res_products = self.cursor.execute(f"SELECT * FROM Foods WHERE barcode = '{barcode}'").fetchall()
            print(res_products)
            return res_products
        except Exception as e:
            return print("SupermarketDAO : Find Food Error!!\n", e)

    def listAllTransactions(self):
        try:
            temp = None
            res_products = self.cursor.execute('SELECT * FROM Transactions').fetchall()
            for i in range(0, len(res_products) - 1):
                for j in range(1, len(res_products)):
                    if res_products[i][0] > res_products[j][0]:
                        temp = res_products[i]
                        res_products[i] = res_products[j]
                        res_products[j] = temp
            for res in res_products:
                print(res)
            return res_products
        except Exception as e:
            return print("SupermarketDAO : List All Transactions Error!!\nPlease Check Cursor or Connection")

    def displayBarchartOfProductSold(self):
        list_name = []
        list_quantity = []
        dict_tran = dict()
        list_tran = self.cursor.execute('SELECT* FROM Transactions').fetchall()
        for x in list_tran:
            try:
                if dict_tran[x[1]] != 0:
                    before_sale = int(dict_tran[x[1]])
                    dict_tran.update({x[1]: (int(x[2] + before_sale))})
            except KeyError:
                dict_tran[x[1]] = int(x[2])
        for key in dict_tran.keys():
            for res in self.cursor.execute(f"SELECT name FROM Foods WHERE barcode='{key}'"):
                list_name.append(str(res[0]))
                list_quantity.append(int(dict_tran[key]))

        # draw bar chart
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["name", "quantity"])
        for i in range(0, len(list_name)):
            sheet.append([list_name[i], list_quantity[i]])

        chart = BarChart()

        chart_data = Reference(sheet, min_row=1, min_col=2, max_row=len(list_name) + 1, max_col=2)
        category = Reference(sheet, min_col=1, min_row=2, max_col=1, max_row=len(list_name) + 1)
        chart.add_data(chart_data, from_rows=False, titles_from_data=True)
        chart.set_categories(category)
        sheet.add_chart(chart, 'F2')
        workbook.save("./barchart_.xlsx")
        return

    def displayExcelReportOfTransactions(self):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["date", "barcode", "amount"])
        transaction_list = self.listAllTransactions()
        idx = 0
        while True:
            if idx == len(transaction_list):
                break
            sheet.append([transaction_list[idx][0], transaction_list[idx][1], transaction_list[idx][2]])
            idx = idx + 1
        workbook.save("transactions.xlsx")
        self.db.commit()

    def addTransactionToDB(self, transaction):
        self.cursor.execute(
            f"INSERT INTO Transactions VALUES ('{transaction.getDate()}'," f"'{transaction.getBarcode()}',"
            f"{int(transaction.getAmount())})")
        self.db.commit()

    def disconnect(self):
        self.cursor.close()
        self.db.commit()
        self.db.close()
