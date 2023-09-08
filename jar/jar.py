class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

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

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Must be 1-12")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    jar.deposit(5)
    print(jar)




if __name__ == "__main__":
    main()