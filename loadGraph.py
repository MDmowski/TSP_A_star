from node import Node

def loadFromFile(filename):
    with open(filename, 'r') as inputfile:
        G = set()
        for line in inputfile:
            parsedLine = line.split(' ')
            if len(parsedLine) != 2:
                raise IOError
            cords = tuple(float(cord) for cord in parsedLine)
            newNode = Node(cords)
            G.add(newNode)

        for node in G:
            node.neighbours = [neighbour for neighbour in G if neighbour != node]

        return G

if __name__ == '__main__':
    loadFromFile('cords.txt')


