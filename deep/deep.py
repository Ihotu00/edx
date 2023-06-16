# accept user input, change to lowercase and remove white spaces
reply = input("""What is the answer to the Great Question of Life,\
the Universe and Everything?\n""")
reply = reply.lower().strip()
# check input to determine correct output
if reply == "42" or reply == "forty two" or reply == "forty-two":
    print("Yes")
else:
    print("No")