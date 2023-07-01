import requests
import sys

if len(sys.argv) == 2:
    if float(sys.argv[1]):
        print("OK")
else:
    sys.exit()
