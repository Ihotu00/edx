class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Must be 1-12")
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.capacity

    def deposit(self, n):
        size += n
        if size <= self.capacity:
            return size
        else:
            raise ValueError("At capacity")

    def withdraw(self, n):
        size -= n
        if size >= 0:
            return size
        else:
            raise ValueError("Not enough")

    # @property
    # def capacity(self):

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = 0


def main():
    cap = int(input("Capacity: "))
    deposit = int(input("Deposit: "))
    print(Jar(cap), Jar(cap).deposit(deposit))




if __name__ == "__main__":
    main()