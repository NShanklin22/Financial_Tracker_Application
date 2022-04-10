# Import Packages
from datetime import datetime
import http.client
import requests
import mimetypes
import json
import csv

def getSilverValue():
    # Set date and time
    now = datetime.now()
    today = datetime.today()

    # Credentials
    a = open('creds/silver.json')
    creds = json.load(a)
    token = creds['token']
    content = creds['type']
    url = creds['url']
    base = creds['base']
    symbol = creds['symbol']

    # Get Data
    conn = http.client.HTTPSConnection(url)
    payload = ''
    headers = {
        'x-access-token': f'{token}',
        'Content-Type': f'{content}'
    }
    conn.request("GET", f"/api/{base}/{symbol}", payload, headers)
    res = conn.getresponse()

    # Result from JSON
    data = json.loads(res.read())

    SilverValue = data['price']

    return SilverValue

def getGoldValue():
    # Set date and time
    now = datetime.now()
    today = datetime.today()
    # Credentials
    a = open('creds/gold.json')
    creds = json.load(a)
    token = creds['token']
    content = creds['type']
    url = creds['url']
    base = creds['base']
    symbol = creds['symbol']

    # Get Data
    conn = http.client.HTTPSConnection(url)
    payload = ''
    headers = {
        'x-access-token': f'{token}',
        'Content-Type': f'{content}'
    }
    conn.request("GET", f"/api/{base}/{symbol}", payload, headers)
    res = conn.getresponse()

    # Result from JSON
    data = json.loads(res.read())
    GoldValue = data['price_gram_24k']

    return GoldValue

def getBTCValue():
    # Set date and time
    now = datetime.now()
    today = datetime.today()

    # Credentials
    a = open('creds/btc.json')
    creds = json.load(a)
    url = creds['url']

    # Get Data
    res = requests.get(url)
    data = res.json()
    BTCValue = data['USD']['last']
    return BTCValue
