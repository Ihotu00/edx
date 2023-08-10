from datetime import date
import re, sys, inflect

def main():
    print(minutes(input("Enter birthday: ")))

def minutes(birthday):
    p = inflect.engine()
    if re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", birthday):
        minutes = int((date.today() - date.fromisoformat(birthday)).total_seconds() / 60)
        return f'{p.number_to_words(minutes, andword="").capitalize()} minutes'
    else:
        sys.exit()


if __name__ == "__main__":
    main()
