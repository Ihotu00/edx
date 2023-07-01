

def main():
    while True:
        level = input("Level: ")
        if check(level):
            break

def check(s):
    try:
        t = int(s)
        return t
    except ValueError:
        pass

if __name__ == "__main__":
    main()