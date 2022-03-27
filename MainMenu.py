import pandas as pd
import numpy as np
import matplotlib as plt
import sqlalchemy
import sqlite3
import datetime
from datetime import datetime
#pd.options.mode.chained_assignment = None  # default='warn'

# Create connection to SQL and an engine for SQLalchemy
connection = sqlite3.connect('data\Portfolio.db')
cursor = connection.cursor()
engine = sqlalchemy.create_engine('sqlite:///data\Portfolio.db').connect()

df = pd.read_sql_table('PortfolioData', engine, index_col=1)

def selectAsset():
    assets = ['btc','cash','gold','silver','spy']
    while True:
        asset = input('Please select an asset from {}: '.format(assets))
        if asset == "gold" or asset == "silver" or asset == "btc" or asset == "spy" or asset == "cash":
            break
        else:
            print("That is not a valid asset, please try again")
    return asset

def assetValue(asset):
    while True:
        quantity = input('Please enter ammount of {} currently held in $: '.format(asset))
        if quantity.isnumeric():
            break
        else:
            print("That is not a valid ammount")
    return quantity

def updateDf(df,asset,quantity):
    new_row = df.iloc[-1].copy()
    print(new_row.head())
    new_row['date'] = datetime.today().date()
    new_row[asset] = quantity
    print(new_row.head())
    # Append the main dataframe with the new row
    df = df.append(new_row, ignore_index=True)
    # Sort values by date
    df.sort_values('date', inplace=True)
    # Merge the data for duplicate dates
    df = df.groupby(['date'], as_index=False).max()
    return df

def addNewEntry():
    global df
    asset = selectAsset()
    quantity = assetValue(asset)
    df = updateDf(df,asset,quantity)
    df.to_sql('PortfolioData', engine, if_exists='replace', index=False)


addNewEntry()
