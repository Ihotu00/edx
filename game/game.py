from random import randint

def check(s)
    while True:
        try:
            s = int(input("Level: "))
            break
        except ValueError:
            pass
while True:
    try:
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
