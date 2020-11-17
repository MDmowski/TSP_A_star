import loadGraph

def buildVisitedNodes(node):
    unvisitedNodes = set()
    # while node.cameFrom:
    #     unvisitedNodes.add(node.cameFrom)
    #     node = node.cameFrom
    while node:
        unvisitedNodes.add(node)
        node = node.cameFrom

    return unvisitedNodes
        
startNode, G = loadGraph.loadFromFile('cords.txt')

openNodes = {startNode} 
closedNodes = set() 

startNode.gScore = 0
startNode.fScore = startNode.calculateFScore(startNode.gScore, startNode, G.difference(buildVisitedNodes(startNode)))

while openNodes:
    current = min(openNodes)

    openNodes.remove(current)
    closedNodes.add(current)
    # unvisitedNodes.discard(current) # Doesn't return an error if node not in set
    unvisitedNodes = G.difference(buildVisitedNodes(current))

    print('Current node: ', current)
    print('Open: ', openNodes)
    print('Closed: ', closedNodes)
    print('Unvisited: ', unvisitedNodes)
    
    if not unvisitedNodes:
        print('\n\nFinished. All nodes:')
        while current:
            print(current)
            current = current.cameFrom
        break

    for neighbour in current.neighbours:
        tentativeGScore = current.gScore + current.distance(neighbour)


        deleted = False
        if neighbour in unvisitedNodes:
            unvisitedNodes.discard(neighbour)
            deleted = True
        print(unvisitedNodes)
        tentativeFScore = neighbour.calculateFScore(tentativeGScore, startNode, unvisitedNodes)

        if deleted:
            unvisitedNodes.add(neighbour)
        print(f'\tNeighbour: {neighbour}')
        print(f'\tgScore: {neighbour.gScore} -> {tentativeGScore}')
        print(f'\tfScore: {neighbour.fScore} -> {tentativeFScore}')

        if tentativeFScore < neighbour.fScore:
            neighbour.cameFrom = current
            neighbour.gScore = tentativeGScore
            neighbour.fScore = tentativeFScore
            openNodes.add(neighbour)
    print()

print('fail')

# print('\n\nFinished. All nodes:')
# for node in closedNodes:
#     print(node, ' -> ', node.cameFrom.number)
