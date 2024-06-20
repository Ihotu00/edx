from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
if len(sys.argv) == 1:
    s = input("Input: ")
    print(figlet.renderText(s))

elif len(sys.argv) == 3:
    if sys.argv[2] in figlet.getFonts() and sys.argv[1] == '-f':
        f = Figlet(font = sys.argv[2])
        s = input("Input: ")
        print(f.renderText(s))
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")
