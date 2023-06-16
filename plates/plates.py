def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # function to check the length is between 2-6
    def length(s):
        if len(s) > 6 or len(s) < 2:
            return 0
        else:
            return 1

    # function to check that the first 2 characters are letters
    def first(s):
        if s[:2].isalpha():
            return 1
        else:
            return 0

    # function to check if there are punctuations or spaces in the string
    def no_special(s):
        for c in s:
            if c in "',.;:?! ":
                return 0
        else:
            return 1

     # function to check if the first number is zero
    # and to check that the numbers are only at the end

    def numbers(s):
        for c in s:
            if c in "0123456789":
                b = s[s.find(c):]
                # return b
                if b[0] == "0" or b.isnumeric() == False:
                    return 0
                else:
                    return 1

        else:
            return 1

    # call all the functions and assign them to variables
    first = first(s)
    length = length(s)
    numbers = numbers(s)
    no_special = no_special(s)
    # compare the variables to check that they are all the same
    if first == length == numbers == no_special:
        return True
    else:
        return False


main()