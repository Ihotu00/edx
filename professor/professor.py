from random import randint

def main():
    l = get_level
    print(generate_integer(l))

def get_level():
    level = 0
    while (level < 1 or level > 3):
        level = int(input("Level: "))
    return level

def generate_integer(level):
    if level == 1:
        x = randint(1, 9)
        y = randint(1, 9)
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    else:
        x = randint(100, 999)
        y = randint(100, 999)
    return x, y


main()