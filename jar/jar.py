class Jar:
    def __init__(self, capacity=-12):
        if capacity < 1:
            raise ValueError("Must be 1-12")

def main():
    Jar(input("Capacity: "))