import math  # Compare floats


class Node:
    def __init__(self, number, cords):
        self.neighbours = []
        self.cords = cords
        self.number = number

    def distance(self, other):
        return math.sqrt(math.pow(self.cords[0]-other.cords[0], 2)+math.pow(self.cords[1]-other.cords[1], 2))

    def __sub__(self, other):
        return self.distance(other)

    def __repr__(self):
        return f'Node{self.number}{self.cords}'

if __name__ == '__main__':
    pass
