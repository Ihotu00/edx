# TODO

letters = sentences = 0
words = 1


def main():
    text = input("Text: ")
    counter(text)

    # apply the Coleman-Liau index

    grade = round((0.0588 * (letters / words) * 100) - (0.296 * (sentences / words) * 100) - 15.8)

    # print correct response

    if grade >= 1 and grade <= 16:
        print(f"Grade {grade}")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print("Grade 16+")


def counter(text):
    global letters, words, sentences
    for char in text.lower():  # loop through input
        if char.isalpha():  # increment letters if alpha
            letters += 1
        elif char.isspace():  # increment words if space
            words += 1
        elif char in [".", "!", "?"]:  # increment sentences if .?!
            sentences += 1


if __name__ == "__main__":
    main()