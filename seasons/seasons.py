from datetime import date, timedelta
import re
import sys

def main():
    sec = input("Enter birthday: ")
    if fullmatch(r"%d{4}-%d{2}-%d{2}", sec):
        min = (date.today() - date.fromisoformat(sec)).total_seconds() / 60
        print(min)
    else:
        sys.exit()

if __name__ == "__main__":
    main()
