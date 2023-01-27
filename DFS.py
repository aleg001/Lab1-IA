"""
Lab#1
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""

from Framework import Framework
from collections import defaultdict


class DFS(Framework):
    # Basado en
    # https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    # https://www.youtube.com/watch?v=sTRK9mQgYuc&t=0s&ab_channel=LearningOrbis
    # https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/depth-first-search-dfs-algorithm/

    def __init__(self, matrix):
        self.originalMatrix = matrix

        self.visitado = []
        self.stack = []

        self.graph = defaultdict(list)

        inicio, fin, v = self.gen_relaciones(matrix)
        self.inicio = inicio
        self.fin = fin

        self.path = self.results(inicio, fin)

        self.test = self.goalTests(inicio, fin)

    def añadir_conexión(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def gen_relaciones(self, matrix):

        inicio = 0
        fin = 0
        vertices = 0
        self.MtoGtoM = []

        pos = 0
        for x in range(len(matrix)):
            temp = []
            for y in range(len(matrix[x])):

                temp.append(pos)

                if matrix[x][y] == 1:
                    # es el inicio
                    inicio = pos

                if matrix[x][y] == 3:
                    # es el fin
                    fin = pos

                if matrix[x][y] != 2:

                    # abajo
                    try:
                        if matrix[x + 1][y] != 2:
                            # si no es una pared
                            qConected = ((x + 1) * len(matrix[x])) + (
                                y
                            )  # Número del otro estado
                            self.añadir_conexión(pos, qConected)
                            vertices += 1

                    except:
                        pass
                        # El otro estado es una pared, por lo que no se genera
                        # conexión

                    # derecha
                    try:
                        if matrix[x][y + 1] != 2:
                            # si no es una pared
                            qConected = (x * len(matrix[x])) + (
                                y + 1
                            )  # Número del otro estado
                            self.añadir_conexión(pos, qConected)
                            vertices += 1

                    except:
                        pass
                        # El otro estado es una pared, por lo que no se genera
                        # conexión

                pos += 1

            self.MtoGtoM.append(temp)

        return (inicio, fin, vertices)

    def goalTests(self, inicio, fin, path=[], visited=set()) -> bool:
        path.append(inicio)
        visited.add(inicio)

        if inicio == fin:
            return path

        for n in self.graph[inicio]:
            if n not in visited:
                result = self.goalTests(n, fin, path, visited)
                if result is not None:
                    return True
        path.pop()
        return False

    def stepCost(self, **kargs) -> int:
        stepCost = 0
        for s in self.path:
            stepCost += 1
        return stepCost

    def pathCost(self, s) -> int:
        stepCost = 0
        for p in s:
            stepCost += 1
        return stepCost

    def action(self, v, visited=set()):

        visited.add(v)

        for n in self.graph[v]:
            if n not in visited:
                self.action(n, visited)

        return visited

    # Returns array path from inicio to fin
    def results(self, inicio, fin, path=[], visited=set()):

        path.append(inicio)
        visited.add(inicio)

        if inicio == fin:
            return path

        for n in self.graph[inicio]:
            if n not in visited:
                result = self.results(n, fin, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None

    def getFullMatrix(self):
        for x in range(len(self.originalMatrix)):
            for y in range(len(self.originalMatrix[x])):

                # Gracias a la matriz MtoGtoM no es necesario
                # hacer el cálculo inverso para conseguir la 
                # posición de cada objeto en la matriz, por lo
                # que ahora solo se revisa si este valore está
                # en la matriz de posiciones y el array path. 
                # Si lo está agrega un número 5 para poder
                # dibujar el path. 

                if self.MtoGtoM[x][y] == self.inicio or self.MtoGtoM[x][y] == self.fin:
                    pass

                elif self.MtoGtoM[x][y] in self.path:
                    self.originalMatrix[x][y] = 5

        return self.originalMatrix


Test_Matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# print("bfs")
# dfs = DFS(Test_Matrix)
# print(dfs.path)
# for x in dfs.MtoGtoM:
#     print(x)

# print('step cost: ', dfs.stepCost())
# print('path cost: ', dfs.pathCost(dfs.path))

# print('Pass test: ', dfs.test)

# print(dfs.action(0))

# for x in dfs.getFullMatrix():
#     print(x)
