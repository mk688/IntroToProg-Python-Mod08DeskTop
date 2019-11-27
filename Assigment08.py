# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MKim, 11.26.2019, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product():
    """Stores data about a product:
    properties:
        ProductName: (string) with the products's  name
        ProductPrice: (float) with the products's standard price
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MKim, 11.26.2019, Modified code to complete assignment 8
    """
    # -- Constrictor --
    # Each object instance can hold the product name and price
    def __init__(self, ProductName, ProductPrice):
        self.name = ProductName
        self.price = ProductPrice

# End of Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        SaveDataToFile(file_name, list_of_product_objects):
        ReadDataFromFile(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MKim, 11/26.2019, Modified code to complete assignment 8
    """

    # -- Methods --
    @staticmethod
    def ReadDataFromFile(filename):
        lstOfProductObjects = []
        file = open(filename,"r")
        for line in file:
            data = line.split(",")
            ProductObject = Product(data[0].strip(), float(data[1].strip()))
            row = {"Name":ProductObject.name, "Price":ProductObject.price}
            lstOfProductObjects.append(row)
        file.close()
        return lstOfProductObjects

    @staticmethod
    def SaveDataToFile(filename, lstOfProductObjects):
        with open(filename, 'w') as file:
            for row in lstOfProductObjects:
                file.write(row["Name"] + "," + str(row["Price"]) + "\n")

# End of Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:

    '''
    Methods: ShowMenu: Showing the user options
             GetUserChoice: Accepting the user's choice
             ShowCurrentData: Showing the current data in file
             GetProductData: Getting a new product name and price from the user
    changelog: (When,Who,What)
        MKim, 11/26.2019, Modified code to complete assignment 8
    '''

    @staticmethod
    def ShowMenu():
        print('''
        Menu of Options
        1)Show current data from the file
        2)Add a product to the list of product objects
        3)Save current data to file and exit
        ''')
        print()

    @staticmethod
    def GetUserChoice():
        choice = input("Which option would you like to perform? ")
        return choice

    def ShowCurrentDataFromFile(self):
        lstOfProductObjects = FileProcessor.ReadDataFromFile(self)
        for row in lstOfProductObjects:
            print(row["Name"] + "," + str(row["Price"]) + "\n")

    @staticmethod
    def GetProductData(lstOfProductObjects):
        newProductName = input("Which product would you like to add? ")
        newProductPrice = float(input("What is the price for the product? "))
        row = {"Name": newProductName, "Price": newProductPrice}
        lstOfProductObjects.append(row)
        return lstOfProductObjects

# End of Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.ReadDataFromFile(strFileName)

while True:
    # Show user a menu of options
    IO.ShowMenu()
    # Get user's menu option choice
    choice = IO.GetUserChoice()

    # Show user current data in the list of product objects
    if choice == "1":
        IO.ShowCurrentDataFromFile(strFileName)

    # Let user add data to the list of product objects
    elif choice == "2":
        lstOfProductObjects = IO.GetProductData(lstOfProductObjects)

    # let user save current data to file and exit program
    elif choice == "3":
        FileProcessor.SaveDataToFile("products2.txt",lstOfProductObjects)
        break
    else:
        try:
            raise TypeError("Invalid Choice")
        except TypeError as te:
            print (te, "Type 1-3 only!")

# End of Main Body of Script  ---------------------------------------------------- #

