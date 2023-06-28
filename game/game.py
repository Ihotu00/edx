from random import randint

def main()
while True:
    try:
        level = int(input("Level: "))
        break
    except ValueError:
        pass

number = randint(1, level)

def check(guess):
    while(True):
        try:
            guess = int(input("Guess: "))
            return guess
        except ValueError:
            pass


    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break

