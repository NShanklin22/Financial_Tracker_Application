import pandas as pd
import numpy as np
import matplotlib as plt
import sqlalchemy
import sqlite3
import datetime
from datetime import datetime
from Functions import *
from getMetalValue import *

# pd.options.mode.chained_assignment = None  # default='warn'

# Create connection to SQL and an engine for SQLalchemy
def updateAssetValues(AssetValues,AssetHoldings):
    assetNames = ['btc','cash','gold','silver','spy']
    assetUnits = ['btc_qty','cash_$','gold_g','silver_oz','spy_qty']

    today = pd.to_datetime(datetime.today().date())

    assets = ['btc_qty','cash_$','gold_g','silver_oz','spy_qty']
    CurrentValues = {'btc':getBTCValue(),'cash':1,'gold':getGoldValue(),'silver':getSilverValue(),'spy':43.42}

    for i in range(len(assetUnits)):
        AssetValues.at[today,assetNames[i]] = CurrentValues[assetNames[i]] * AssetHoldings.at[today,assetUnits[i]]

    print("Current Asset Values:\n")
    print(AssetValues.tail(1))
    print("\n")
    return AssetValues