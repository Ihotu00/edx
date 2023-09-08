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
    def size(self=0):
        return self._size

def main():
    cap = int(input("Capacity: "))
    withdraw = int(input("Withdraw: "))
    print(Jar(cap), Jar(cap).withdraw(withdraw))




if __name__ == "__main__":
    main()