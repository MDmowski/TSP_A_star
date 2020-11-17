from node import Node

def loadFromFile(filename):
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

        # G.remove(startNode)

        return startNode, G

if __name__ == '__main__':
    print(loadFromFile('cords.txt'))


