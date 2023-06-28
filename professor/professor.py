from random import randint

def get_level():
    level = 0
    while (level < 1 or level > 3):
        level = int(input("Level: "))

def generate_integer(level):
    x = randint