"""
Lab#1
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""
from Framework import Framework


class BFS(Framework):
    # Basado en https://www.geeksforgeeks.org/shortest-path-unweighted-graph/
    def __init__(self, matrix):
        self.visited = []
        self.queue = []

        self.graph = [[] for i in range((len(matrix)) * len(matrix))]

        inicio, fin, v = self.gen_relaciones(matrix)
        self.inicio = inicio
        self.fin = fin
        self.v = v

        self.results((inicio, fin), v)

    def añadir_conexión(self, fuente, destino):

        self.graph[fuente].append(destino)
        self.graph[destino].append(fuente)

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

    # Interface implementation

    def action(self, s) -> str:
        return super().action(s)

    def results(self, s, a) -> int:

        inicio, fin = s
        v = a

        # predecesor y distancia
        pred = [0 for i in range(v)]
        dist = [0 for i in range(v)]

        s = (self.graph, inicio, fin, v, pred, dist)

        if self.goalTests(s) == False:
            print("no")

        self.path = []
        crawl = fin
        self.path.append(crawl)

        # CORREGIR CORREGIR
        while pred[crawl] != -1:
            self.path.append(pred[crawl])
            crawl = pred[crawl]
            # print(crawl)

        # print("Camino corto tamaño: ", dist[fin])
        # for x in range(len(self.path) - 1, -1, -1):
        #     print(self.path[x])

        self.stepCost = dist[fin]

        return self.path

    def goalTests(self, s) -> bool:

        relaciones, fuente, destino, v, pred, dist = s

        # Conjunto de todos los vértices adyacentes que se encuentran en la frontera
        cola = []

        # Conjutno de vértices ya visitados.
        visitados = [False for i in range(v)]

        for i in range(v):

            dist[i] = 1000000
            pred[i] = -1

        visitados[fuente] = True
        dist[fuente] = 0
        cola.append(fuente)

        # Algoritmo BFS estándar
        while len(cola) != 0:
            u = cola[0]
            cola.pop(0)

            for i in range(len(relaciones[u])):
                if visitados[relaciones[u][i]] == False:
                    visitados[relaciones[u][i]] = True
                    dist[relaciones[u][i]] = dist[u] + 1
                    pred[relaciones[u][i]] = u
                    cola.append(relaciones[u][i])

                    # Se para si se encuentra el destino
                    if relaciones[u][i] == destino:
                        return True

        return False

    def stepCost(self) -> int:
        step_cost = 0
        for x in self.path:
            step_cost += 1
        return step_cost

    def pathCost(self, s) -> int:
        path_cost = 0
        for x in s:
            path_cost += 1
        return path_cost


# Test_Matrix = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 2, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 2, 0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 2, 3, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# print("bfs")
# bfs = BFS(Test_Matrix)
# for x in bfs.MtoGtoM:
#     print(x)
# path = bfs.path
# for p in path:
#     print(p)
# cost = bfs.pathCost(path)
# print('path cost: ', cost)

# # stepCost = bfs.stepCost()
# print('stepCost: ', cost)

# bfs.action("")
