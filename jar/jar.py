class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Must be 1-12")
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.capacity

    def deposit(self, n):
        self.n += n
        if self.n <= 12:
            return self.n
        else:
            raise ValueError("At capacity")

    def withdraw(self, n):
        self.n -= n
        if self.n >= 0:
            return self.n
        else:
            raise ValueError("Not enough")

    # @property
    # def capacity(self):

def main():
    cap = int(input("Capacity: "))
    withdraw = int(input("Withdraw: "))
    print(Jar(cap), Jar(cap).withdraw(withdraw))




if __name__ == "__main__":
    main()