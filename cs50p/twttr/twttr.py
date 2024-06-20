def main():
    string1 = input("Input: ")
    print(f"Output: {shorten(string1)}")

def shorten(string1):
    string2 = ""
    # loop to remove all vowels
    for i in range(len(string1)):
        # use function isconsonant to check character
        if isconsonant(string1[i]):
            # add character to string2
            string2 += string1[i]
    return string2

# function to check if a character is a vowel


def isconsonant(char):
    char = char.lower()
    if char in ["a", "e", "i", "o", "u"]:
        return False
    else:
        return True


if __name__ == "__main__":
    main()