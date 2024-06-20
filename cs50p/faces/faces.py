# accept user input and replace emoticons with emojis
feels = input("How are you feeling? \n", )
feels = feels.replace(":)", "🙂").replace(":(", "🙁")
print(feels)