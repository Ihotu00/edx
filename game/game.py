from random import randint


def main():
    level = check(int(input("Level: ")))
    guess = int(input("Guess: "))


while True:
    try:
        break
    except ValueError:
        pass

number = randint(1, level)

while(True):
    try:
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass


