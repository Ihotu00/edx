import requests
import sys

if len(sys.argv) == 2:
    try:
        float(sys.argv[1])
        print("OK")
    except ValueError:
        sys.exit()
# else:
#     sys.exit()
