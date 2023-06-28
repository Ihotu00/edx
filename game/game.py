from random import randint

level = input("Level: ")
guess = input("Guess: ")
number = randint(1, level)
if guess < number:
    print("Too small!")
elif guess > number:
    print("Too large!")
else:
    print("Just right!")