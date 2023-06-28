from random import randint

while True:
    try:
        level = int(input("Level: "))
        guess = int(input("Guess: "))
        break
    except ValueError:
        pass
number = randint(1, level)
if guess < number:
    print("Too small!")
elif guess > number:
    print("Too large!")
else:
    print("Just right!")
    