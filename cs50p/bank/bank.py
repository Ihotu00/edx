def main():
    # get input from user, change to lowercase and remove whitespaces
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.strip().lower()
    # check for "hello in greeting"
    if greeting.find("hello") != -1:
        return 0
    # check that first character is "h" and "hello" isn't in greeting
    elif greeting[0].find("h") != -1 and greeting.find("hello") == -1:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()