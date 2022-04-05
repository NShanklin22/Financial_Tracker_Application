import pandas as pd
import datetime
from datetime import datetime

#def selectAsset():
#     assets = ['btc','cash','gold','silver','spy']
#     while True:
#         asset = input('Please select an asset from {}: '.format(assets))
#         if asset == "gold" or asset == "silver" or asset == "btc" or asset == "spy" or asset == "cash":
#             break
#         else:
#             print("That is not a valid asset, please try again")
#     return asset
#
# def assetValue(asset):
#     while True:
#         quantity = input('Please enter ammount of {} currently held in $: '.format(asset))
#         if quantity.isnumeric():
#             break
#         else:
#             print("That is not a valid ammount")
#     return quantity
#
# def updateDf(df,asset,quantity):
#     new_row = df.iloc[-1].copy()
#     print(new_row.head())
#     new_row['date'] = datetime.today().date()
#     new_row[asset] = quantity
#     print(new_row.head())
#     # Append the main dataframe with the new row
#     df = df.append(new_row, ignore_index=True)
#     # Sort values by date
#     df.sort_values('date', inplace=True)
#     # Merge the data for duplicate dates
#     df = df.groupby(['date'], as_index=False).max()
#     return df
#
# def addNewEntry():
#     global df
#     asset = selectAsset()
#     quantity = assetValue(asset)
#     df = updateDf(df,asset,quantity)
#     df.to_sql('PortfolioData', engine, if_exists='replace', index=False)

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

def printMenu():
    print("Menu Options")
    print("-----------------------")
    print("1 - Update assets")
    print("2 - View data")
    print("3 - Analyze data")
    print("----------------------")
