# Import Packages
from datetime import datetime
import http.client
import mimetypes
import json
import csv

Holdings = {'gold':int(6)}

# Timestamp
now = datetime.now()
today = datetime.today()
print("Date Success!")

# Credentials
a = open('./cred.json')
creds = json.load(a)
token = creds['token']
content = creds['type']
url = creds['url']
base = creds['base']
symbol = creds['symbol']
print("Credentials Success!")

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
AssetValue = data['price_gram_24k']

TotalValue = AssetValue * Holdings['gold']

print(TotalValue)