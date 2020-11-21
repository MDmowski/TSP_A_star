from node import Node

def loadGraph(filename):
    with open(filename, 'r') as inputfile:
        G = set()
        num = 0
        for line in inputfile:
            parsedLine = line.split(' ')
            if len(parsedLine) != 2:
                raise IOError
            cords = tuple(float(cord) for cord in parsedLine)
            newNode = Node(num, cords)
            if num == 0:
                startNode = newNode
            num += 1
            G.add(newNode)

        for node in G:
            node.neighbours = [neighbour for neighbour in G if neighbour != node]

        return startNode, G

def savePath(filename, path):
    with open(filename, 'w') as outputfile:
        if path:
            for node in path:
                outputfile.write(f'{node.cords[0]} {node.cords[1]}\n')
            node = path[0]
            outputfile.write(f'{node.cords[0]} {node.cords[1]}\n')

if __name__ == '__main__':
    pass


