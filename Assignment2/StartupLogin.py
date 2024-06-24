import os
import sqlite3
from SupermarketDAO import SupermarketDAO
import Product_Class
import atexit

supermarketDAO = SupermarketDAO()
supermarketDAO.initDB()
conn = supermarketDAO.db
cur = supermarketDAO.cursor


def when_exit():
    supermarketDAO.disconnect()
    #sdfadf asdasdf


def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        statement = f"SELECT Username FROM Users WHERE Username='{username}' AND Password='{password}'"
        cur.execute(statement)
        if not cur.fetchone():
            os.system('cls')
            print("\n")
            print(f"Login failed for user {username}: Try again")
            print("\n")
            print("Press enter to attempt to login again\n")
        else:
            return

if __name__ == "__main__":
    login_result = login()
    # When Exit, Disconnect Database
    atexit.register(supermarketDAO.disconnect)
    while True:
        print("1. Add Products to Database")
        print("2. List all Products in Database (ascending order of barcode)")
        print("3. Find a Product in the Database, based on Product Bar-Code")
        print("4. List All Transactions (Ascending order of date of transaction)")
        print("5. Display a Bar chart of Products sold by quantity")
        print("6. Display an Excel report of all transactions")
        print("7. Exit")

        sel = int(input("Please select a choice from above: "))

        if sel == 1:
            barcode = input("Please insert a barcode: ")
            name = input("Please insert a product name: ")
            desc = input("Please insert a descriptionad: ")
            price = input("Please insert a price: ")
            supermarketDAO.addProductToDB(Product_Class.Product(barcode, name, desc, price))
        elif sel == 2:
            supermarketDAO.listAllProducts()
        elif sel == 3:
            search = input("Please enter a product barcode to search: ")
            supermarketDAO.findProduct(search)
        elif sel == 4:
            supermarketDAO.listAllTransactions()
        elif sel == 5:
            supermarketDAO.displayBarchartOfProductSold()
            print("Completed inderting barchart")
            print("Wuould you like to select a chioce from above?")
        elif sel == 6:
            supermarketDAO.displayExcelReportOfTransactions()
            print("Completed report of transaction")
            print("Would you like to more select a choice or exit? ")
        elif sel == 7:
            raise SystemExit(0)
