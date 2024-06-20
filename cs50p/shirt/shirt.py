from PIL import Image, ImageOps
import sys
import PIL

name1, ext1 = sys.argv[1].split(".")
name2, ext2 = sys.argv[2].split(".")
ext1 = ext1.lower()

if len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")
elif ext1 != "jpg" and ext1 != "png" and ext1 != "jpeg":
    sys.exit("Invalid extension")
else:
    try:
        pic = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size
pic = ImageOps.fit(pic, size)
pic.paste(shirt, shirt)
pic.save(sys.argv[2])
