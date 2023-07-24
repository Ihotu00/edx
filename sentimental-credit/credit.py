import re

# TODO
def main():
    card = input("card: ")
    # if check_sum(card) == 0:
    #     pattern(card)
    # else:
    check_sum(card)

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
    sum = 0
    for i in reversed(range(0, len(card), 2)):
        digit = int(card[i])
        digit *= 2
        # sum += digit
    # for i in reversed(range(1, len(card), 2)):
    #     digit = int(card[i])
    #     sum += digit
    # return sum
        print(digit)



if __name__ == "__main__":
    main()
# amex:378282246310005, visa:4111111111111111, 4003600000000014 master: 5555555555554444