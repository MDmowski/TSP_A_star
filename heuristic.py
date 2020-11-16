from node import Node
import math


def createEdge(srcNode, destNode):
    dist = srcNode - destNode 
    edge = {
        'srcNumber' : srcNode.number,
        'destNumber' : destNode.number,
        'weight' : dist
    }
    return edge


def mst(unvisited):
    edges = []
    maxNumber = 1
    for src in unvisited:
        for dest in src.neighbours:
            if dest in unvisited:
                if (src.number > maxNumber):
                    maxNumber = src.number
                if(dest.number > maxNumber):
                    maxNumber = dest.number
                edges.append(createEdge(src, dest))
    mst = []
    cost = 0
    edges = sorted(edges, key=lambda item: item['weight'])
    tree_id = list(range(maxNumber+1))

    for edge in edges:
        if(tree_id[edge['srcNumber']] != tree_id[edge['destNumber']]):
            cost += edge['weight']
            mst.append(edge)
            old_id = tree_id[edge['srcNumber']]
            new_id = tree_id[edge['destNumber']]
            for i, current_id in enumerate(tree_id):
                if(current_id == old_id):
                    tree_id[i] = new_id
    print(mst)
    return cost


def heuristic(start, unvisited):
    mst_cost = mst(start, unvisited)
    # closestNeighbour = start.neighbours[0]
    # minDist = start - closestNeighbour
    # for dest in start.neighbours:
    #     dist = start - dest
    #     if(dist < minDist):
    #         minDist = dist 

    # The same as above but with generator expression
    minDist = min(start - dest for dest in start.neighbours)

    return mst_cost + start.gScore + minDist


if __name__ == '__main__':
    start = Node(0, (0, 0))
    a = Node(1, (0, 1))
    b = Node(2, (1, 0))
    c = Node(3, (1, 1))
    d = Node(4, (-1, 0))
    start.neighbours = [a, b]
    a.neighbours = [start, b]
    b.neighbours = [start, a, c]
    c.neighbours = [b, d]
    d.neighbours = [c]
    unvisited = [a, b, c, d]

    print(mst(unvisited))
