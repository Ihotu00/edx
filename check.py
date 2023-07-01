import sys

def main():
    check(sys.argv[1])

def check(s):
    while True:
        try:
            t = int(input(f"{s=}: "))
            return True
        except ValueError:
            pass

main()