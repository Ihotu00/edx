import sys

num = 0

# get correct argv
if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif (sys.argv[1][-2:] != "py"):
    sys.exit("Not a python file")
else:
    try:
        file = open(sys.argv[1], "r") #open file if it exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    for line in file:
        if not line.lstrip().startswith("#") and line.strip(): #eliminate commets and blank lines
            num  += 1
    print(num)
file.close()