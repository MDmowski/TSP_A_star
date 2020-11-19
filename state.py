import heuristic

class State:
    def __init__(self, path, length, graph):
        self.path = path
        self.length = length
        self.graph = graph

        self.unvisitedNodes = self.graph.difference(path)

        self.fScore = length + heuristic.calculateFScore(self.startNode(), self.currentNode(), self.unvisitedNodes) 

    def __lt__(self, other):
        return self.fScore < other.fScore

    def __repr__(self):
        pathString = '' 
        for node in self.path:
            pathString += (str(node.number)+'->')

        return f'State: {pathString} {self.fScore}'

    def exportState(filename):
        pass

    def currentNode(self):
        return self.path[-1]

    def startNode(self):
        return self.path[0]

    def isFinal(self):
        return not bool(self.unvisitedNodes)

    def expand(self):
        nextStates = set()

        nextNodes = ( nextNode for nextNode in self.currentNode().neighbours if nextNode in self.unvisitedNodes )

        for nextNode in nextNodes:
            newPath = self.path.copy()
            newPath.append(nextNode)
            newLength = self.length + (nextNode - self.currentNode())
            newState = State(newPath, newLength, self.graph)
            nextStates.add(newState)

        return nextStates


        
        


