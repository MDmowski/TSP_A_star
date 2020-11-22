import graphIO
from state import State


def bruteForce(startNode, G):
    startState = State([startNode], 0, G)

    openStates = {startState} 
    closedStates = set() 

    CUTOFF = 500000

    while openStates:
        if len(openStates) > CUTOFF:
            return None
        currentState = openStates.pop()

        closedStates.add(currentState)

        openStates.update(currentState.expand())

    solution = min(state for state in closedStates if state.isFinal())
    print(solution)
    return solution.getCycleLength()
