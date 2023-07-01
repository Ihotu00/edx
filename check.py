

def main():
   check()

def check():
    while True:
        try:
            t = int(input(f": "))
            return t
        except ValueError:
            pass

main()