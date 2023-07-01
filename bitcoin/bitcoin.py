import requests
import sys
import json

if len(sys.argv) == 2:
    try:
        float(sys.argv[1])
        # print("OK")
    except ValueError:
        sys.exit()

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

bpi = response.json()["bpi"]
usd = bpi["USD"]
amount = sys.argv[1] *
print(amount)
