import requests
import sys
import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit()
try:
    sys.argv[1] = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bpi = response.json()["bpi"]
usd = bpi["USD"]
amount = sys.argv[1] * usd["rate_float"]
print(f"${amount:,.4f}")
