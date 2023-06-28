import inflect

p = inflect.engine()
names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print("\n")
        break
print(names)