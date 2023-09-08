class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Must be 1-12")

    def __str__(self):
        return ""

def main():
    cap = int(input("Capacity: "))
    Jar(cap)



if __name__ == "__main__":
    main()