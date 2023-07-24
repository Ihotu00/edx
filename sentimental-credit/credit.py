import re

# TODO
def main():
    card = input("card: ")
    # if check_sum(card) == 0:
    #     pattern(card)
    # else:
    #     print("INVALID")
    # print(check_sum(card))
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
    temp = card[:len(card) - 1]
    for i in temp[ : :-2]:
    #     digit = int(temp[i])
    #     digit *= 2
    #     for i in str(digit):
    #         sum += int(i)
    # for i in card[ : :-2]:
    #     digit = int(card[i])
    #     sum += digit
    # return sum % 10
        print(i)



if __name__ == "__main__":
    main()
# amex:378282246310005, 371449635398431
# visa:4222222222222, 4111111111111111 master: 5555555555554444