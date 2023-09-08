class Jar:
    def __init__(self, capacity=12):
        if not int(capacity):
            raise ValueError("Must be 1-12")

def main():
    Jar(input("Capacity: "))