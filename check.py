

def main():
   level = check(input("Level: "))

def check(s):
    try:
        t = int(s)
        return True
    except ValueError:
        return False

main()