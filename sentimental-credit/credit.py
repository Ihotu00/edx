import re

# TODO
pattern = "^(34|37)\d{13}"
card = input("card: ")
match = re.match(pattern, card)
if match:
    print("AMEX")
else:
    print("wrong")
