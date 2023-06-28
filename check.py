import sys

def main():
    check(sys.argv[1])

def check(s):
    while True:
        try:
            t = int(input("s: "))
            break
        except ValueError:
            pass
    print(t)

main()