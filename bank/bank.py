# get input from user, change to lowercase and remove whitespaces
greeting = input("Greeting: ")
greeting = greeting.strip().lower()

# check for "hello in greeting"
if greeting.find("hello") != -1:
    print("$0")
# check that first character is "h" and "hello" isn't in greeting
elif greeting[0].find("h") != -1 and greeting.find("hello") == -1:
    print("$20")
else:
    print("$100")