from state import State
import heuristic

class AStarState(State):
    def __init__(self, path, length, graph):
        super().__init__(path, length, graph)

        self.fScore = length + heuristic.calculateFScore(self.startNode(), self.currentNode(), self.unvisitedNodes) 

    def createNewState(self, newPath, newLength):
        return AStarState(newPath, newLength, self.graph)

    def __lt__(self, other):
        return self.fScore < other.fScore
