class DFS:
    # Basado en https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    def __init__(self, matrix):
        self.visitado = []
        self.stack = []

        self.graph = [[] for i in range((len(matrix)) * len(matrix))]

    def dfs(self, v, grafo):
        if v not in self.visitado:
            for i in g[v]:
                self.dfs(g, i)

    def algoritmo(self):

        visitados = set()
        for v in self.grafo:
            if v not in visitados:
                self.dfs(v, visitados)

        return False


Test_Matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 3, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
]

print("bfs")
bfs = DFS(Test_Matrix)
# print(bfs.graph)
