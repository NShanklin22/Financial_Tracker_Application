import pandas as pd
import numpy as np
import matplotlib as plt
import sqlalchemy
import sqlite3
import datetime
import time
from datetime import datetime
from Functions import *
from updateAssetValues import *

# pd.options.mode.chained_assignment = None  # default='warn'

# Create connection to SQL and an engine for SQLalchemy
connection = sqlite3.connect('data\Portfolio.db')
cursor = connection.cursor()
engine = sqlalchemy.create_engine('sqlite:///data\Portfolio.db').connect()

AssetHoldings = pd.read_sql_table('AssetHoldings', engine, index_col='date')
AssetValues = pd.read_sql_table('AssetValues', engine, index_col='date')

global assets
assets = ['btc_qty', 'cash_$', 'gold_g', 'silver_oz', 'spy_qty']


def mainMenu(AssetHoldings, AssetValues):
    MenuOption = int(getMenuOption())
    if (MenuOption == 1):
        updateHoldings(AssetHoldings, AssetValues)
        return
    elif (MenuOption == 2):
        dataMenu(AssetHoldings, AssetValues)
        return
    elif (MenuOption == 3):
        print("Lets analyze some data")
        analyzeData()
        return


def updateHoldings(AssetHoldings, AssetValues):
    today = pd.to_datetime(datetime.today().date())
    AssetHoldings.at[today] = AssetHoldings.iloc[-1]
    match = False
    while not match:
        asset = input("Please enter the asset you would like to update {}: ".format(assets))
        for i in range(len(assets)):
            if assets[i] == asset:
                try:
                    quantity = float(input("Please enter the quantity of {} currently held: ".format(assets[i])))
                    AssetHoldings.at[today, assets[i]] = quantity
                    print(AssetHoldings.tail(1))
                    response = input("Would you like to update another asset (Y/N)? ")
                    if (response == 'Y'):
                        continue
                    else:
                        match = True
                except:
                    print("That is not a valid quantity")

    print("Saving holdings to database...")
    time.sleep(2)
    AssetHoldings.to_sql('AssetHoldings', engine, if_exists='replace', index=True, index_label="date")
    print("Holdings saved to database")
    print("Updating Asset Values...\n")
    time.sleep(2)
    AssetValues = updateAssetValues(AssetValues, AssetHoldings)
    print("Asset values updated successfully")
    print("Saving asset values to database...")
    time.sleep(2)
    AssetValues.to_sql('AssetValues', engine, if_exists='replace', index=True, index_label="date")
    print("Asset values saved to database!")


def dataMenu(df):
    MenuOption = int(getDataMenu())
    if (MenuOption == 1):
        print("\nCurrent Holdings:\n")
        print(AssetHoldings)
        print("\nReturning to the Main Menu \n")
    elif (MenuOption == 2):
        print("Reading data from the database")
        print("\nReturning to the Main Menu \n")

    mainMenu(df)


def readData():
    return


def analyzeData():
    return


mainMenu(AssetHoldings, AssetValues)
