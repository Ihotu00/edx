import re

# TODO
def main():
    card = input("card: ")
    if check_sum(card) == 0:
        pattern(card)
    else:
        print("INVALID")

def pattern(card):

    # re for card pattern

    amex = "^(34|37)\d{13}$"
    visa = "^(4)(\d{12}$|\d{15}$)"
    master = "^(51|55)\d{14}$"

    # matching input to pattern

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
    temp = card[:len(card) - 1]  # store input in variable without last digit

    for i in temp[ : :-2]:  # first half of the check_sum: iterate through every other digit
        digit = int(i)      # and multiply by 2
        digit *= 2
        for i in str(digit):
            sum += int(i)   # add each digit to sum
    for i in card[ : :-2]:  # second half of check_sum: iterate through the other digits
        digit = int(i)
        sum += digit
    return sum % 10     # return last digit of sum



if __name__ == "__main__":
    main()