amount = 50
print("Amount Due:", amount)
while amount != 0:
    # loops until input = 25, 10 or 5
    while True:
        coin = int(input("Insert coin: "))
        # check that input is correct
        if coin == 25 or coin == 10 or coin == 5:
            break
        else:
            print("Amount Due:", amount)
    # calculate the amount due
    amount -= coin
    # print the amount due if amount is greater than 0
    if amount > 0:
        print("Amount Due:", amount)
    # print the absolute value of amount as change owed when amount < 0
    elif amount <= 0:
        print("Change Owed:", abs(amount))
        break