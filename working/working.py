import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.fullmatch(r"([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)", s):

        start, meridiem1, to, stop, meridiem2 = s.split(" ")

        if ":" in start:
            hour, minutes = start.split(":")
            if meridiem1 == "PM" and hour != "12":
                hour = int(hour) + 12
                start = f"{hour}:{minutes}"
            elif meridiem1 == "AM" and hour == "12":
                start = "00:00"
            else:
                start = f"{int(hour):02d}:{minutes}"
        else:
            if meridiem1 == "PM" and start != "12":
                start = f"{int(start) + 12}:00"
            elif meridiem1 == "AM" and start == "12":
                start = "00:00"
            else:
                start = f"{int(start):02d}:00"

        if ":" in stop:
            hour, minutes = stop.split(":")
            if meridiem2 == "PM" and hour != "12":
                hour = int(hour) + 12
                stop = f"{hour}:{minutes}"
            elif meridiem2 == "AM" and hour == "12":
                stop = "00:00"
            else:
                stop = f"{int(hour):02d}:{minutes}"
        else:
            if meridiem2 == "PM" and stop != "12":
                stop = f"{int(stop) + 12}:00"
            elif meridiem2 == "AM" and stop == "12":
                stop = "00:00"
            else:
                stop = f"{int(stop):02d}:00"

        return f"{start} to {stop}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()