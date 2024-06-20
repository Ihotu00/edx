# accept input and pass it to function 'convert'
def main():
    time = convert(input("What time is it? "))
# check time and print appropriate output
    if time >= 7 and time <= 8:
        print("Breakfast Time")
    elif (time >= 12 and time <= 13) or (time >= 1 and time <= 2):
        print("Lunch Time")
    elif (time >= 18 and time <= 19) or (time >= 6 and time <= 7):
        print("Dinner Time")
    else:
        print("")

# function to remove 'am' or 'pm' and split argument to 'hour' and 'minute'


def convert(t):
    t = t.strip("ampm")
    hour, minute = t.split(":")
    hour = float(hour)
    minute = float(minute)
    minute = round(minute * 0.01666, 2)  # converts the minutes to decimal

    t = hour + minute
    return t


if __name__ == "__main__":
    main()