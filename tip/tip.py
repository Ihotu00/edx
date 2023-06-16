# accept user input and pass to function


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# convert user input to float and remove '$'


def dollars_to_float(d):
    d = float(d.lstrip("$"))
    return d

# convert input to float and remove '%'


def percent_to_float(p):
    p = float(p.rstrip("%"))/100
    return p


main()