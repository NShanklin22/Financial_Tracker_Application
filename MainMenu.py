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

df = pd.read_sql_table('PortfolioData', engine, index_col='date')

global assets
assets = ['btc','cash','gold','silver','spy']

def mainMenu(df):
    MenuOption = int(getMenuOption())
    if (MenuOption == 1):
        updateAssets(df)
        return
    elif (MenuOption == 2):
        print("Reading data from the database")
        readData()
        return
    elif (MenuOption == 3):
        print("Lets analyze some data")
        analyzeData()
        return

def getMenuOption():
    printMenu()
    while True:
        MenuOption = input("Please select a menu option: ")
        if MenuOption.isdigit() and (int(MenuOption) == 1 or int(MenuOption) == 2 or int(MenuOption) == 3):
            return MenuOption
        else:
            print("That is not a valid option")

def updateAssets(df):
    today = datetime.today().date()
    new_row = getNewRow(assets,today)
    new_row['total'] = new_row.sum(axis=1)
    df = new_row
    df.iloc[today] = new_row
    df.to_sql('PortfolioData', engine, if_exists='replace', index=True, index_label="date")

def readData():
    return


def analyzeData():
    return


mainMenu(df)
