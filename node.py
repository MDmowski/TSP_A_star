import math  # Compare floats


class Node:
    def __init__(self, number, cords):
        self.neighbours = []
        self.cords = cords
        self.number = number
        self.backRef = None
        self.fScore = float('inf')
        self.gScore = float('inf')

    def calcuteFScore(self, unvisitedNodes):
        self.fScore = self.gScore + h(unvistedNodes)

    def distance(self, other):
        return math.sqrt(math.pow(self.cords[0]-other.cords[0], 2)+math.pow(self.cords[1]-other.cords[1], 2))

    def __lt__(self, other):
        return self.fScore < other.fScore

    def __repr__(self):
        return f'Node{self.cords}: {self.fScore}'

    # def __eq__(self, other):
    #     return (math.isclose(self.cords[0], other.cords[0]) and
    #             math.isclose(self.cords[1], other.cords[1]))

    def __sub__(self, other):
        return self.distance(other)

if __name__ == '__main__':
    a = Node((2.161161, 7/3))
    b = Node((2.161161, 7/3 * 10 / 10))

    print(a == b)
