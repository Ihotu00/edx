# TODO

# get name

name = input("What is your name?\n")

# print hello, {name}
if "," in name:
    last, first = name.split(",")
    name = f"{first} {last}"

print("hello,", name)