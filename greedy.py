import loadGraph
from state import State


def greedy():
    startNode, G = loadGraph.loadFromFile('cords.txt')

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
            break
        currentState = min((state for state in newStates),key=lambda state: state.length - currentState.length)



if __name__ == '__main__':
    greedy()
