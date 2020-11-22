import time

from timeout import timeout
from astar import astar
from bruteForce import bruteForce
from greedy import greedy

import graphIO
import pandas


@timeout(180)
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
    MIN_NUM_OF_NODES = 5
    MAX_NUM_OF_NODES = 26
    NUM_OF_NODES_TO_REPEAT = 20
    NUM_OF_REPS = 30

    rows = []

    for nodesNumber in range(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES + 1):
        startNode, G = graphIO.generateRandomGraph(nodesNumber)
        row = []
        row.append(nodesNumber)
        try:
            row.extend(timeFunction(astar, startNode, G))
        except TimeoutError:
            row.extend((None, None))
        try:
            row.extend(timeFunction(greedy, startNode, G))
        except TimeoutError:
            row.extend((None, None))
        try:
            row.extend(timeFunction(bruteForce, startNode, G))
        except TimeoutError:
            row.extend((None, None))
        print(row)
        rows.append(row)

    for _ in range(NUM_OF_REPS):
        startNode, G = graphIO.generateRandomGraph(NUM_OF_NODES_TO_REPEAT)
        row = []
        row.append(NUM_OF_NODES_TO_REPEAT)
        try:
            row.extend(timeFunction(astar, startNode, G))
        except TimeoutError:
            row.extend((None, None))
        try:
            row.extend(timeFunction(greedy, startNode, G))
        except TimeoutError:
            row.extend((None, None))
        row.extend((None, None))
        print(row)
        rows.append(row)

    columns = ['nodes_number', 'astar_time', 'astar_length', 'greedy_time', 'greedy_length', 'brute_time', 'brute_length']
    df = pandas.DataFrame(rows, columns=columns)
    df.to_pickle('timeData.pkl')

if __name__ == '__main__':
    runTests()

