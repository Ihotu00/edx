

def main():
   level = check(level)

def check(s):
    while True:
        try:
            t = int(input(f"{s=}: "))
            return True
        except ValueError:
            pass

main()