import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'src="(https?://(www\.)?youtube.com/embed/.+?)"', s)
    if matches:
        src = matches.group(0).strip('"').rsplit("/", maxsplit=1)
        tmp = "https://youtu.be/" + src[1]
        return tmp



if __name__ == "__main__":
    main()

# <iframe src="https://www.youtube.com/embed/xvFZjo5PgGO"><iframe>
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>