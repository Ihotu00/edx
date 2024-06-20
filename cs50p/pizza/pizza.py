import sys
import csv
from tabulate import tabulate

# get correct cmdline arg
if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif (sys.argv[1][-3:] != "csv"):
    sys.exit("Not a csv file")
else:
    try:
        file = open(sys.argv[1], "r") #open file if it exist
    except FileNotFoundError:
        sys.exit("File does not exist")

reader = csv.reader(file)
print(tabulate(reader, headers="firstrow", tablefmt="grid"))
file.close()