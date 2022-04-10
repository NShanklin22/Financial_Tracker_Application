import pandas as pd
import datetime
from datetime import datetime

def getMenuOption():
    printMainMenu()
    while True:
        MenuOption = input("Please select a menu option: ")
        if MenuOption.isdigit() and (int(MenuOption) == 1 or int(MenuOption) == 2 or int(MenuOption) == 3):
            return MenuOption
        else:
            print("That is not a valid option")

def getDataMenu():
    printDataMenu()
    while True:
        MenuOption = input("Please select a menu option: ")
        if MenuOption.isdigit() and (int(MenuOption) == 1 or int(MenuOption) == 2):
            return MenuOption
        else:
            print("That is not a valid option")

def getNewRow(assets,today):
    new_row = pd.DataFrame(index=[today])
    confirm = False
    while not confirm:
        for i in range(len(assets)):
            new_row[assets[i]] = float(input("Please enter a value in $ for {}: ".format(assets[i])))
        print(new_row.head())
        response = input("Does this look correct? (Y/N): ")
        if response == "Y":
            confirm = True
        elif response == "N":
            confirm = False
        else:
            print("That is not a valid response")
    return new_row

def printMainMenu():
    print("-----------------------")
    print("Main Menu")
    print("-----------------------")
    print("1 - Update assets")
    print("2 - View data")
    print("3 - Analyze data")
    print("----------------------")

def printDataMenu():
    print("-----------------------")
    print("Data Menu")
    print("-----------------------")
    print("1 - View current assets")
    print("2 - View asset values")
    print("----------------------")

