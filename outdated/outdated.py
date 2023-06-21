# list of all months
month = ["January", "Febuary", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]
# loop forever
while True:
    date = input("Date: ")
    # split into month, day and year of "/" is in input
    if "/" in date:
        m, d, y = date.split("/")
        try:
            # check the integer value of month and date are correct
            if int(m) <= 12 and int(m) >= 1 and int(d) <= 31 and int(d) >= 1:
                break
        except ValueError:
            pass
    elif "," in date:
        # remove "," and split input to month day and year
        m, d, y = date.replace(",", "").split(" ")
        # change month tp the integer equivalent using list 'month'
        if m in month:
            m = month.index(m) + 1
        try:
            if m <= 12 and m >= 1 and int(d) <= 31 and int(d) >= 1:
                break
        except TypeError:
            pass

# print date
print(f"{int(y)}-{int(m):02}-{int(d):02}")