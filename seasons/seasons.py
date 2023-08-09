from datetime import date

class Date:
    def __init__(self, birthday):
        self.birthday = birthday
    def __sub__(date.today(), birthday):
        return date.today() - birthday

def main():
    Date(input("Enter birthday: "))
    # birthday = input("Enter birthday: ")
    # print(operator.__sub__(date.today(), birthday))

if __name__ == "__main__":
    main()