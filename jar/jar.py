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

    def withdraw(self, n):
        self.capacity -= n
        if self.capacity >= 0:
            return self.capacity
        else:
            raise ValueError("Not enough")

    @property
    def capacity(self):

def main():
    cap = int(input("Capacity: "))
    withdraw = int(input("Withdraw: "))
    print(Jar(cap), Jar(cap).withdraw(withdraw))




if __name__ == "__main__":
    main()