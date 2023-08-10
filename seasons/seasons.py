from datetime import date, timedelta, datetime
import operator

class Date:
    def __init__(self, birthday):
        self.birthday = date.fromisoformat(birthday)
        operator.sub(date.today(), self.birthday)
        # return (date.today() - self.birthday).total_seconds()

def main():
    sec = input("Enter birthday: ")
    min = (date.today() - date.fromisoformat(sec)).total_seconds() / 60
    print(min)

if __name__ == "__main__":
    main()


    # 2000-04-15