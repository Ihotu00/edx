i = 1
# empty dictionary
list = {}
while True:
    try:
        item = input().upper()
    # accept input until user enters ctrl + d
    except EOFError:
        # print out dictionary in alphabetical order
        for key, value in sorted(list.items()):
            print(value, key.upper())
        break
    # increase the value if key is already in list
    if item in list:
        i += 1
        list[item] = i
    # assign input as key and value as 1 in dictionary
    else:
        list[item] = 1
