class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Must be 1-12")
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        if self.size <= self.capacity:
            return self.size
        else:
            raise ValueError("At capacity")

    def withdraw(self, n):
        self.size -= n
        if self.size >= 0:
            return self.size
        else:
            raise ValueError("Not enough")

    # @property
    # def capacity(self):

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self.size = 0


def main():
    cap = int(input("Capacity: "))
    deposit = int(input("Deposit: "))
    print(Jar(cap), Jar(cap).deposit(deposit))




if __name__ == "__main__":
    main()