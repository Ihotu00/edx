from random import randint


def main():
    level = check(input("Level: "))
    guess = check(input("Guess: "))
    number = randint(1, level)
    while True:
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def check(s):
    while True
        try:
            t = int(s)
            return True
        except ValueError:
            return False


main()

