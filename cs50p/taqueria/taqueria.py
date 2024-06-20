# dictionary with menu items and respective prices
menu = {
    "Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00,
    "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50,
    "Taco": 3.00, "Tortilla Salad": 8.00
}

price = 0
while True:
    try:
        item = input("Item: ").title()
    # accept more input until used presses ctrl + d
    except (EOFError):
        print("\n")
        break
    if item in menu:
        # add price of each input
        price += menu[item]
        print(f"${price:.2f}")