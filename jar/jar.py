class Jar:
    def __init__(self, capacity=-12):
        if capacity < 1:
            raise ValueError("Must be 1-12")

def main():
    cap = input("Capacity: ")
    Jar(cap)

if __name__ == "__main__":
    main()