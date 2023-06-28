from random import randint

def check(s)
    while True:
        try:
            type = int(s)
            return True
        except ValueError:
            pass

number = randint(1, level)
if guess < number:
    print("Too small!")
elif guess > number:
    print("Too large!")
else:
    print("Just right!")
