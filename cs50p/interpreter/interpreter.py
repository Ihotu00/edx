# accept user input and split into variables
expression = input("Expression: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)
# check y for the appropriate operator
if y == "+":
    answer = round(x + z, 1)
    print(answer)
elif y == "-":
    answer = round(x - z, 1)
    print(answer)
elif y == "*":
    answer = round(x * z, 1)
    print(answer)
elif y == "/":
    answer = round(x / z, 1)
    print(answer)
else:
    print(" ")