import graphIO
from AStarState import AStarState


def astar(filename):
    startNode, G = graphIO.loadGraph(filename)

    startState = AStarState([startNode], 0, G)

    openStates = {startState} 
    closedStates = set() 

    while openStates:
        currentState = min(openStates)

        openStates.remove(currentState)
        closedStates.add(currentState)

        if currentState.isFinal():
            print(currentState)
            return(currentState.getCycleLength())
            graphIO.savePath(currentState.path)
            break

        openStates.update(currentState.expand())
