from random import randint
from check import check

def main():
    i = 0
    score = 0
    fail = 0

    l = get_level()

    while (i < 10):
        val1, val2 = generate_integer(l)
        asum = val1 + val2

        for fail in range(3):
            sum = check(input(f"{val1} + {val2} = "))
            if sum == asum:
                score += 1
                break
            else:
                fail +=1
                print("EEE")
                if fail == 3:
                    print(asum)
        i += 1

    print("Score: ", score)

def get_level():
    while True:
       level = check(input("Level: "))
       break
    if (level >= 1 and level <= 3):
        return level



def generate_integer(level):
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    else:
        x = randint(100, 999)
        y = randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()