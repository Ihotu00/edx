from random import randint


while True:
    try:
        level = input("Level: ")
    try:
        guess = input("Guess: ")
        break
    except ValueError:
        pass

number = randint(1, level)
while(True):
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break

