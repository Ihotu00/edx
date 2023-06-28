from random import randint

level = int(input("Level: "))
guess = int(input("Guess: "))
number = randint(1, level)
if guess < number:
    print("Too small!")
elif guess > number:
    print("Too large!")
else:
    print("Just right!")