from datetime import date, timedelta

def main():
    sec = input("Enter birthday: ")
    min = (date.today() - date.fromisoformat(sec)).total_seconds() / 60
    print(min)

if __name__ == "__main__":
    main()
