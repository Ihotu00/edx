# accept name, change to lowercase and remove whitespaces
name = input("What is the name of your file? ").lower().strip()
# split name after last occurrence of "." and store in variables
a, b, c = name.rpartition(".")
# match c to corresponding output
match c:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
