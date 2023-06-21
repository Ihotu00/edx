def main():
    a, b = seperate()
    z = a / b * 100
    # check z and print appropriate output
    if z > 1 and z < 99:
        print(f"{z:.0f}%")
    elif z <= 1:
        print("E")
    else:
        print("F")

# function to seperate user input


def seperate():
    while True:
        fuel = input("How much left: ")
        x, sign, y = fuel.partition("/")
        # make sure x and y are integers
        try:
            x, y = int(x), int(y)
            if x <= y:
                return x, y
        # continue loop if input is not integer or y = 0
        except (ValueError, ZeroDivisionError):
            pass


main()
