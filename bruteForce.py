import graphIO
from state import State


def bruteForce(filename):
    startNode, G = graphIO.loadGraph(filename)

    startState = State([startNode], 0, G)

    openStates = {startState} 
    closedStates = set() 

    while openStates:
        currentState = openStates.pop()

        closedStates.add(currentState)

        openStates.update(currentState.expand())

    solution = min(state for state in closedStates if state.isFinal())
    print(solution)
    return(solution.getCycleLength())
    graphIO.savePath(solution.path)
