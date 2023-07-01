

def main():
   level = check()

def check(s):
    while True:
        try:
            t = int(s)
            return True
        except ValueError:
            pass

main()