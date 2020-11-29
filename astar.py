import graphIO
import sys
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
            return currentState.getCycleLength(), len(closedStates)
            break

        openStates.update(currentState.expand())

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 astar.py filename')
    else:
        startNode, G = graphIO.loadGraph(sys.argv[1])

        length, closedStatesNumber = astar(startNode, G)

        print(f'Solution length: {length}\nNumber of closed states: {closedStatesNumber}')





