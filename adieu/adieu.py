import inflect

p = inflect.engine()
names = ["Adieu", "adieu" "to"]
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print("\n")
        break
print(p.join(names))