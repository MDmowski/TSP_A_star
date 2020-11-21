class State:
    def __init__(self, path, length, graph):
        self.path = path
        self.length = length
        self.graph = graph

        self.unvisitedNodes = graph.difference(path)


    def __lt__(self, other):
        return self.getCycleLength() < other.getCycleLength()

    def __repr__(self):
        pathString = '' 
        for node in self.path:
            pathString += (str(node.number)+'->')

        return f'State: {pathString} {self.getCycleLength()}'

    def getCycleLength(self):
        return self.length + (self.startNode() - self.currentNode())

    def exportState(filename):
        pass

    def currentNode(self):
        return self.path[-1]

    def startNode(self):
        return self.path[0]

    def isFinal(self):
        return not bool(self.unvisitedNodes)

    def createNewState(self, newPath, newLength):
        return State(newPath, newLength, self.graph)


    def expand(self):
        nextStates = set()

        for nextNode in self.currentNode().neighbours:
            if nextNode in self.unvisitedNodes:
                newPath = self.path.copy()
                newPath.append(nextNode)
                newLength = self.length + (nextNode - self.currentNode())
                newState = self.createNewState(newPath, newLength)
                nextStates.add(newState)

        return nextStates


        
        


