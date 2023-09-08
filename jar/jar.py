class Jar:
    def __init__(self, n, capacity=12):
        if not int(n):
            raise ValueError("Must be 1-12")
        self.n = n