import sys
import csv

# get correct cmdline arg
if len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few arguments")
else:
    try:
        file = open(sys.argv[1], "r") #open file if it exist
    except FileNotFoundError:
        sys.exit("File does not exist")

reader = csv.DictReader(file)

with open(sys.argv[2], "w") as out_file:
    write = csv.DictWriter(out_file, fieldnames=["first", "last", "house"])
    write.writeheader()
    for row in reader:
        last, first = row["name"].split(" ")
        house = row["house"]
        write.writerow({"first": first, "last": last.strip(',"'), "house": house})

file.close()