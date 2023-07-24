import re

# TODO
def main():
    card = input("card: ")
    pattern(card)

def pattern(card):
    amex = "^(34|37)\d{13}$"
    visa = "^(4)(\d{12}$|\d{15}$)"
    master = "^(51|55)\d{14}$"
    if re.match(master, card):
        print("MASTERCARD")
    elif re.match(amex, card):
        print("AMEX")
    elif re.match(visa, card):
        print("VISA")
    else:
        print("INVALID")

def check_sum(card):
    for i in range(len(card), -2):
        



if __name__ == "__main__":
    main()
# amex:378282246310005, visa:4111111111111111, master: 5555555555554444