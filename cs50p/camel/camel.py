camel = input("camelCase: ")
snake = ""
# loop to convert input to snake_case
for i in range(len(camel)):
    # check for uppercase
    if camel[i].isupper():
        # add _ before the uppercase character and insert to snake
        snake += "_" + camel[i]
    else:
        # put the rest of the input to snake unchanged
        snake += camel[i]
# print out snake in lowercase
print("snake_case: ", snake.lower())
