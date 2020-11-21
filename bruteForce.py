import loadGraph
from state import State


def bruteForce():
    startNode, G = loadGraph.loadFromFile('cords.txt')

    startState = State([startNode], 0, G)

    openStates = {startState} 
    closedStates = set() 

    while openStates:
        currentState = openStates.pop()

        closedStates.add(currentState)

        openStates.update(currentState.expand())

    print(min((state for state in closedStates if not state.unvisitedNodes), key=lambda state: state.fScore))

if __name__ == '__main__':
    bruteForce()
