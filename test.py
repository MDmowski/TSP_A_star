import time

from timeout import timeout
from astar import astar
from bruteForce import bruteForce
from greedy import greedy

import graphIO
import pandas


@timeout(180)
def timeAlgorithm(function, *args):
    tic = time.perf_counter()
    returnValue = function(*args)
    toc = time.perf_counter()

    if returnValue[0]:
        elapsedTime = toc - tic
    else:
        elapsedTime = None
    

    length, closedStates = returnValue
    return elapsedTime, length, closedStates 

def runTests():
    MIN_NUM_OF_NODES = 5
    MAX_NUM_OF_NODES = 26
    NUM_OF_NODES_TO_REPEAT = [10, 20]
    NUM_OF_REPS = 30


    rows = []

    for nodesNumber in range(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES + 1):
        startNode, G = graphIO.generateRandomGraph(nodesNumber)
        row = []
        row.append(nodesNumber)
        try:
            row.extend(timeAlgorithm(astar, startNode, G))
        except TimeoutError:
            row.extend((None, None, None))
        try:
            row.extend(timeAlgorithm(greedy, startNode, G))
        except TimeoutError:
            row.extend((None, None, None))
        try:
            row.extend(timeAlgorithm(bruteForce, startNode, G))
        except TimeoutError:
            row.extend((None, None, None))
        print(row)
        rows.append(row)

    for nodesNum in NUM_OF_NODES_TO_REPEAT:
        for _ in range(NUM_OF_REPS):
            startNode, G = graphIO.generateRandomGraph(nodesNum)
            row = []
            row.append(nodesNum)
            try:
                row.extend(timeAlgorithm(astar, startNode, G))
            except TimeoutError:
                row.extend((None, None, None))
            try:
                row.extend(timeAlgorithm(greedy, startNode, G))
            except TimeoutError:
                row.extend((None, None, None))
            row.extend((None, None, None))
            print(row)
            rows.append(row)

    columns = ['nodes_number', 'astar_time', 'astar_length', 'astar_closed', 'greedy_time', 'greedy_length', 'greedy_closed', 'brute_time', 'brute_length', 'brute_closed']
    df = pandas.DataFrame(rows, columns=columns)
    df.to_pickle('timeData.pkl')

if __name__ == '__main__':
    runTests()

