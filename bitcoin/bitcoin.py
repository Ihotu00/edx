import requests
import sys
from check import check

if len(sys.argv) == 2:
    if check(sys.argv[1]):
        print("OK")
else:
    sys.exit()
