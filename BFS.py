class BFS():
    # Basado en https://www.geeksforgeeks.org/shortest-path-unweighted-graph/
    def __init__(self, matrix):
        self.visited = []
        self.queue = []

        self.graph = [[] for i in range((len(matrix)) * len(matrix))]

        inicio, fin, v = self.gen_relaciones(matrix)
        print('v: ',v)
        print('inicio: ',inicio)
        print('fin: ',fin)
        for x in self.MtoGtoM:
            print(x)
        for x in self.graph:
            print(x)

        self.conseguir_ruta(inicio, fin, v)

    def añadir_conexión(self, fuente, destino):

        self.graph[fuente].append(destino)
        self.graph[destino].append(fuente)

    def conseguir_ruta(self, inicio, fin, v):

        # predecesor y distancia
        pred=[0 for i in range(v)]
        dist=[0 for i in range(v)]

        if(
            self.algoritmo(
                relaciones = self.graph,
                fuente = inicio,
                destino = fin,
                v = v,
                pred=pred,
                dist=dist
            ) == False
        ):
            print('no')

        path = []
        crawl = fin
        path.append(crawl)

        # CORREGIR CORREGIR
        while (pred[crawl] != -1):
            path.append(pred[crawl])
            crawl = pred[crawl]
            # print(crawl)

        print("Camino corto tamaño: ", dist[fin])
        for x in range(len(path) -1, -1, -1):
            print(path[x])



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

                if (matrix[x][y] == 2):
                    # es el inicio
                    inicio = (pos)

                if (matrix[x][y] == 3):
                    # es el fin
                    fin = (pos)

                if matrix[x][y] != 1:

                    # abajo
                    try:
                        if matrix[x + 1][y] != 1:
                            # si no es una pared
                            qConected = ((x + 1) * len(matrix[x])) + (y) # Número del otro estado
                            self.añadir_conexión(pos, qConected)
                            print('abajo :',pos, qConected)
                            vertices += 1

                    except: 
                        pass
                        # El otro estado es una pared, por lo que no se genera 
                        # conexión

                    # derecha
                    try:
                        if matrix[x][y + 1] != 1:
                            # si no es una pared
                            qConected = (x * len(matrix[x])) + (y + 1) # Número del otro estado
                            self.añadir_conexión(pos, qConected)
                            print('derecha :',pos, qConected)
                            vertices += 1

                    except: 
                        pass
                        # El otro estado es una pared, por lo que no se genera 
                        # conexión

                pos += 1

            self.MtoGtoM.append(temp)
                

        return (inicio, fin, vertices)
        

    def algoritmo(self, relaciones, fuente, destino, v, pred, dist):

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
        while (len(cola) != 0):
            u = cola[0]
            cola.pop(0)

            for i in range(len(relaciones[u])):
                if (visitados[relaciones[u][i]] == False):
                    visitados[relaciones[u][i]] = True
                    dist[relaciones[u][i]] = dist[u] + 1
                    pred[relaciones[u][i]] = u
                    cola.append(relaciones[u][i])

                    # Se para si se encuentra el destino
                    if (relaciones[u][i] == destino):
                        return True

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

print('bfs')
bfs = BFS(Test_Matrix)
# print(bfs.graph)

