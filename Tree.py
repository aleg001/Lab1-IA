"""
Lab#1

Módulo de árboles
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""


class Node:
    def __init__(self, x, y, value) -> None:
        self.f = 0
        self.g = 0
        self.h = 0
        self.x = x
        self.y = y
        self.value = value
        self.succesors = None
        self.explored = False


class Tree:
    def __init__(self, path: list[list]) -> None:
        for row in path:
            if 1 in row:
                self.root = Node(row.index(1), path.index(row), value=1)

        NodeBuffer = [[] for y in range(len(path))]

        for y in range(len(path)):
            for x in range(len(path)):
                NodeBuffer[y].append(Node(x, y, path[y][x]))

        for y in range(len(path)):
            for x in range(len(path)):
                succesors = []
                if x < len(path) - 1:
                    succesors.append(NodeBuffer[y][x + 1])
                if x > 0:
                    succesors.append(NodeBuffer[y][x - 1])
                if x < len(path) - 1 and y < len(path) - 1:
                    succesors.append(NodeBuffer[y + 1][x + 1])
                if x > 0 and y < len(path) - 1:
                    succesors.append(NodeBuffer[y + 1][x - 1])
                if y > 0 and x < len(path) - 1:
                    succesors.append(NodeBuffer[y - 1][x + 1])
                if x > 0 and y > 0:
                    succesors.append(NodeBuffer[y - 1][x - 1])
                if y > 0:
                    succesors.append(NodeBuffer[y - 1][x])
                if y < len(path) - 1:
                    succesors.append(NodeBuffer[y - 1][x])

                NodeBuffer[y][x].succesors = succesors


path = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


x = Tree(path)
