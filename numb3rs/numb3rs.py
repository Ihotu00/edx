import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


# function to check user input for format #.#.#.# with # = 0 - 255

def validate(ip):
    ran = r"(\d{1,2}|1(\d{1,2})|2[0-4]\d|25[0-5])"  # format for 0 - 255
    pattern = ran + r"\." + ran + r"\." + ran + r"\." + ran  # format for #.#.#.#
    if re.fullmatch(pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()