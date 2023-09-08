class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Must be 1-12")
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.capacity

    def deposit(self, n):
        self.capacity += n

def main():
    cap = int(input("Capacity: "))
    print(Jar(cap))




if __name__ == "__main__":
    main()