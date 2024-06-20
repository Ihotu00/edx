# TODO
from cs50 import get_int


def main():
    height = 0
    while height < 1 or height > 8:  # get correct range for height
        height = get_int("Height: ")
    first_pyramid(height)


def first_pyramid(height):  # print out pyramid
    for i in range(height):
        print(" " * (height - i - 1), end="")
        print("#" * (i + 1), end="")
        print(" " * 2, end="")
        print("#" * (i + 1))


if __name__ == "__main__":
    main()
