import math # Compare floats

class Node:
    def __init__(self, cords):
        self.neighbours = []
        self.cords = cords
        self.backRef = None
        self.fScore = float('inf')
        self.gScore = float('inf')

    
    def calcuteFScore(self, unvisitedNodes):
        self.fScore =  self.gScore + h(unvistedNodes)

    def __lt__(self, other):
        return self.fScore < other.fScore

    def __eq__(self, other):
        return (math.isclose(self.cords[0], other.cords[0]) and
                math.isclose(self.cords[1], other.cords[1]))

if __name__ == '__main__':
    a = Node((2.161161, 7/3))
    b = Node((2.161161, 7/3 * 10 / 10))

    print(a == b)

