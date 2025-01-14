import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    sys.argv[1] = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bpi = response.json()["bpi"]
usd = bpi["USD"]
amount = sys.argv[1] * usd["rate_float"]
print(f"${amount:,.4f}")
