import re

# TODO
amex = "^(34|37)\d{13}$"
visa = "^(4)\d{12,}$"
card = input("card: ")
match = re.match(amex, card)
if match:
    print("AMEX")
else:
    print("wrong")


# amex:378282246310005, visa:4111111111111111