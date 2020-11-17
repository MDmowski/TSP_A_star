import math  # Compare floats
import heuristic


class Node:
    def __init__(self, number, cords):
        self.neighbours = []
        self.cords = cords
        self.number = number
        self.cameFrom = None
        self.fScore = float('inf')
        self.gScore = float('inf')

    def calculateFScore(self, gScore, start, unvisitedNodes):
        return gScore + heuristic.calculate(start, self, unvisitedNodes)

    def distance(self, other):
        return math.sqrt(math.pow(self.cords[0]-other.cords[0], 2)+math.pow(self.cords[1]-other.cords[1], 2))

    def __lt__(self, other):
        return self.fScore < other.fScore

    def __repr__(self):
        cameFromNumber = self.cameFrom.number if self.cameFrom else None
        return f'Node{self.number}(came: {cameFromNumber}): g:{self.gScore}, f:{self.fScore}'

    # def __eq__(self, other):
    #     return (math.isclose(self.cords[0], other.cords[0]) and
    #             math.isclose(self.cords[1], other.cords[1]))

    def __sub__(self, other):
        return self.distance(other)

if __name__ == '__main__':
    a = Node((2.161161, 7/3))
    b = Node((2.161161, 7/3 * 10 / 10))

    print(a == b)
