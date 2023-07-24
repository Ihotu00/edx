import re

# TODO
amex = "^(34|37)\d{13}"
visa = "^4\d{13|16}"
card = input("card: ")
match = re.match(visa, card)
if match:
    print("AMEX")
else:
    print("wrong")
