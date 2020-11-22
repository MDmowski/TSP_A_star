import graphIO
from AStarState import AStarState


def astar(startNode, G):
    startState = AStarState([startNode], 0, G)

    openStates = {startState} 
    closedStates = set() 

    while openStates:
        currentState = min(openStates)

        openStates.remove(currentState)
        closedStates.add(currentState)

        if currentState.isFinal():
            print(currentState)
            return currentState.getCycleLength()
            break

        openStates.update(currentState.expand())
