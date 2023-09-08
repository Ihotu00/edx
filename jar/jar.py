class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Must be 1-12")
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.capacity

    def deposit(self, n):
        self.capacity += n
        if self.capacity <= 12:
            return self.capacity
        else:
            raise ValueError("At capacity")

def main():
    cap = int(input("Capacity: "))
    deposit = int(input("Deposit: "))
    print(Jar(cap), Jar(cap).deposit(deposit))




if __name__ == "__main__":
    main()