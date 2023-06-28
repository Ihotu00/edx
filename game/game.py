from random import randint

level = int(input("Level: "))
number = randint(1, level)
while True:
    guess = int(input("Guess: "))
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break