class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Must be 1-12")
        self.capacity = capacity

    def __str__(self):
        for i in range(self.capacity):
            return "🍪"

def main():
    cap = int(input("Capacity: "))
    print(Jar(cap))




if __name__ == "__main__":
    main()