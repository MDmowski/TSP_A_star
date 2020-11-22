import graphIO
from state import State


def greedy(startNode, G):
    startState = State([startNode], 0, G)

    openStates = {startState}
    closedStates = {startState}

    currentState = startState

    while openStates:
        newStates = currentState.expand()
        openStates.update(newStates)
        openStates.remove(currentState)
        closedStates.add(currentState)

        if currentState.isFinal():
            print(currentState)
            return currentState.getCycleLength()
        currentState = min(newStates,key=lambda state: state.length - currentState.length)
