def main():
    fuel = input("How much left: ")
    if convert(fuel):
        z = convert(fuel)
        print(gauge(z))
    else:
        print(convert(fuel))

def convert(fuel):
    x, sign, y = fuel.partition("/")
    try:
        x, y = int(x), int(y)
        z = int(x / y * 100)
        if x > y:
            raise ValueError
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    else:
        return z

def gauge(z):
    if z > 1 and z < 99:
        return f"{str(z)}%"
    elif z <= 1:
        return "E"
    else:
        return "F"


if __name__ == "__main__":
    main()
