from datetime import date, timedelta, datetime
i

class Date:
    def __init__(self, birthday):
        self.birthday = birthday
    operator.sub__(date.today(), self.birthday)
        # return (date.today() - self.birthday).total_seconds()

def main():
    sec = Date(input("Enter birthday: "))
    print(sec.__sub__())
    # sec = input("Enter birthday: ")
    # print((date.today() - sec).total_seconds())

if __name__ == "__main__":
    main()


    # 2000-04-15