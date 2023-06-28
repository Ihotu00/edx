from random import randint

number = randint(1, level)
while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    guess = int(input("Guess: "))
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break