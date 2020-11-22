import node
import math

def createEdge(srcNode, destNode):
    dist = srcNode - destNode 
    edge = {
        'srcNumber' : srcNode.number,
        'destNumber' : destNode.number,
        'weight' : dist
    }
    return edge


def mst(graph):

    if len(graph) < 2:
        return [0]+list(graph)

    edges = []
    maxNumber = 1
    for src in graph:
        for dest in src.neighbours:
            if dest in graph:
                if (src.number > maxNumber):
                    maxNumber = src.number
                if(dest.number > maxNumber):
                    maxNumber = dest.number
                edges.append(createEdge(src, dest))
    mst = []
    cost = 0
    edges = sorted(edges, key=lambda item: item['weight'])
    tree_id = list(range(maxNumber+1))

    appearances = [0]*(maxNumber+1)

    for edge in edges:
        if(tree_id[edge['srcNumber']] != tree_id[edge['destNumber']]):
            cost += edge['weight']
            mst.append(edge)
            old_id = tree_id[edge['srcNumber']]
            new_id = tree_id[edge['destNumber']]
            for i, current_id in enumerate(tree_id):
                if(current_id == old_id):
                    tree_id[i] = new_id
            appearances[edge['srcNumber']] += 1
            appearances[edge['destNumber']] += 1

    singles = []
    for i in range(len(appearances)):
        if appearances[i] == 1:
            singles.append(i)
    ends = list(vertex for vertex in graph if vertex.number in singles)
    return [cost]+ends


def calculateFScore(startNode, currentNode, unvisitedNodes):
    mstResult = mst(unvisitedNodes)
    mst_cost = mstResult.pop(0)
    if len(mstResult) > 1:
        #minDistToStart = min(startNode - neighbour for neighbour in mstResult)
        #minDistToCurrent = min(currentNode - neighbour for neighbour in mstResult)
        minDist = float('inf')
        for vertex in mstResult:
            otherEnds = mstResult[:]
            otherEnds.remove(vertex)
            for otherVertex in otherEnds:
                currentDist = (startNode - vertex) + (currentNode - otherVertex)
                if currentDist < minDist: minDist = currentDist
        return mst_cost + minDist
        # return mst_cost + minDistToStart + minDistToCurrent
    elif mstResult:
        return (currentNode - mstResult[0])+ (startNode - mstResult[0])
    else:
        return startNode - currentNode


if __name__ == '__main__':
    start = node.Node(0, (0, 0))
    a = node.Node(1, (0, 1))
    b = node.Node(2, (1, 0))
    c = node.Node(3, (1, 1))
    d = node.Node(4, (-1, 0))
    start.neighbours = [a, b]
    a.neighbours = [start, b]
    b.neighbours = [start, a, c]
    c.neighbours = [b, d]
    d.neighbours = [c]
    unvisited = [a, b, c, d]

    print(mst(unvisited))
