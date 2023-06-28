from random import randint

def main():
    i = 0
    score = 0
    l = get_level()
    while (i < 10):
        val1, val2 = generate_integer(l)
        sum = input(f"{val1} + {val2}: ")
        try:
            sum = int(sum)
        except ValueError:
            pass
        asum = val1 + val2
        if sum == asum:
            score += 1
        else:
            print("EEE")
        i += 1

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