import loadGraph
from state import State


def astar():
    startNode, G = loadGraph.loadFromFile('cords.txt')

    startState = State([startNode], 0, G)

    openStates = {startState} 
    closedStates = set() 

    while openStates:
        currentState = min(openStates)

        openStates.remove(currentState)
        closedStates.add(currentState)

        if currentState.isFinal():
            print(currentState)
            break

        openStates.update(currentState.expand())
