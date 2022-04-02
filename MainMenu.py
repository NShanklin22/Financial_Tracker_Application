import pandas as pd
import numpy as np
import matplotlib as plt
import sqlalchemy
import sqlite3
import datetime
from datetime import datetime
from Functions import *

# pd.options.mode.chained_assignment = None  # default='warn'

# Create connection to SQL and an engine for SQLalchemy
connection = sqlite3.connect('data\Portfolio.db')
cursor = connection.cursor()
engine = sqlalchemy.create_engine('sqlite:///data\Portfolio.db').connect()

df = pd.read_sql_table('PortfolioData', engine, index_col=1)

def mainMenu():
    MenuOption = getMenuOption()
    if(MenuOption == 1):
        return
    elif(MenuOption == 2):
        return
    elif(MenuOption == 3):
        return

def getMenuOption():
    printMenu()
    while True:
        MenuOption = input("Please select a menu option: ")
        if MenuOption.isdigit() and (int(MenuOption) == 1 or int(MenuOption) == 2 or int(MenuOption) == 3):
            return MenuOption
        else:
            print("That is not a valid option")

def updateAssets():
    return

def readData():
    return

def analyzeData():
    return

mainMenu()
