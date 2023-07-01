

def main():
    while True:
        level = input("Level: ")
        if check(level):
            break

def check(s):
    try:
        t = int(s)
        return True
    except ValueError:
        return False

main()