from datetime import date

def main():
    birthday = input("Enter birthday: ")
    print(__sub__(date.today(), birthday))

if __name__ == "__main__":
    main()