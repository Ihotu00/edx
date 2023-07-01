

def main():
   level = check(level)

def check(s):
    while True:
        try:
            t = int(input(f"{s=}: "))
            return t
        except ValueError:
            pass

main()