import re

# TODO
card = input("card: ")

def pattern():
    amex = "^(34|37)\d{13}$"
    visa = "^(4)(\d{12}$|\d{15}$)"
    master = "^(51|55)\d{14}$"
    match = re.match(master, card)
    if match:
        print("AMEX")
    else:
        print("wrong")



# amex:378282246310005, visa:4111111111111111, master: 5555555555554444