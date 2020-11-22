import time

from timeout import timeout
from astar import astar
from bruteForce import bruteForce
from greedy import greedy

import graphIO


@timeout(2)
def timeFunction(function, *args):
    tic = time.perf_counter()
    returnValue = function(*args)
    toc = time.perf_counter()

    if returnValue:
        elapsedTime = toc - tic
    else:
        elapsedTime = None
    
    return elapsedTime, returnValue


def runTests():
    startNode, G = graphIO.generateRandomGraph(5)
    row = []
    try:
        row.extend(timeFunction(astar, startNode, G))
    except TimeoutError:
        row.extend((None, None))
    try:
        row.extend(timeFunction(astar, startNode, G))
    except TimeoutError:
        row.extend((None, None))
    try:
        row.extend(timeFunction(astar, startNode, G))
    except TimeoutError:
        row.extend((None, None))
    print(row)


if __name__ == '__main__':
    runTests()

