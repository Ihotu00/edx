from datetime import date, timedelta
import re
import sys
import inflect

def main():
    p = inflect.engine()
    sec = input("Enter birthday: ")
    if re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", sec):
        min = int((date.today() - date.fromisoformat(sec)).total_seconds() / 60)
        print(f"{p.number_to_words(min, andword="").capitalize()} minutes")
    else:
        sys.exit()

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/seasons