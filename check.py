import sys



def check(s):
    while True:
        try:
            t = int(input("s: "))
            break
        except ValueError:
            pass
    print(t)

check()