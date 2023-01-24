from Framework import Framework
from collections import defaultdict

class DFS(Framework):
    # Basado en https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    # https://www.youtube.com/watch?v=sTRK9mQgYuc&t=0s&ab_channel=LearningOrbis
    def __init__(self, matrix):
        self.visitado = []
        self.stack = []

        self.graph = defaultdict(list)

        inicio, fin, v = self.gen_relaciones(matrix)

        self.path = self.DFS(inicio, fin)

    # def dfs(self, v, grafo):
    #     if v not in self.visitado:
    #         for i in g[v]:
    #             self.dfs(g, i)

    # def algoritmo(self):

    #     visitados = set()
    #     for v in self.grafo:
    #         if v not in visitados:
    #             self.dfs(v, visitados)

    #     return False

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

    def results(self, s, a) -> int:
        return super().results(s, a)

    def goalTests(self, s) -> bool:
        return super().goalTests(s)

    def stepCost(self, **kargs) -> int:
        return super().stepCost(**kargs)

    def pathCost(self, s) -> int:
        return super().pathCost(s)

    def action(self, v, visited):
        
        visited.add(v)
        print(v, end=" ")

        for n in self.graph[v]:
            if n not in visited:
                self.action(n, visited)

    def DFS(self, inicio, fin, path=[], visited = set()):

        path.append(inicio)
        visited.add(inicio)

        if inicio == fin:
            return path
        
        #self.action(inicio, visited)
        for n in self.graph[inicio]:
            if n not in visited:
                result = self.DFS(n, fin, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None


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

print("bfs")
dfs = DFS(Test_Matrix)
print(dfs.path)
for x in dfs.MtoGtoM:
    print(x)
