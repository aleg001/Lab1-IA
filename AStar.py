"""
Lab#1

Implementacion de algoritmo A*
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""

# ------ Arbol ------
class Node:
  def __init__(self, x, y, value) -> None:
    self.f = 99999
    self.x = x
    self.y = y
    self.value = value
    self.succesors = None

class Tree:
  def __init__(self, path:list[list]) -> None:
    self.size = len(path)
    self.goal:list = []
    NodeBuffer:list[list[Node]] = [[] for y in range(len(path))]

    for y in range(len(path)):
      for x in range(len(path)):
        actual = Node(x, y, path[y][x])
        if actual.value == 3:
          self.goal.append(actual)
        elif actual.value == 1:
          self.root = actual
        
        NodeBuffer[y].append(actual)

    for y in range(len(path)):
      for x in range(len(path)):
        succesors = []
        if x < len(path) - 1:
          if path[y][x+1] != 2:
            succesors.append(NodeBuffer[y][x+1]) 
        if x > 0:
          if path[y][x-1] != 2:
            succesors.append(NodeBuffer[y][x-1])
        if x < len(path) - 1 and y < len(path) - 1:
          if path[y+1][x+1] != 2:
            succesors.append(NodeBuffer[y+1][x+1])
        if x > 0 and y < len(path) - 1:
          if path[y+1][x-1] != 2:
            succesors.append(NodeBuffer[y+1][x-1])
        if y > 0 and x < len(path) - 1:
          if path[y-1][x+1] != 2:
            succesors.append(NodeBuffer[y-1][x+1])
        if x > 0 and y > 0:
          if path[y-1][x-1] != 2:
            succesors.append(NodeBuffer[y-1][x-1])
        if y > 0:
          if path[y-1][x] != 2:
            succesors.append(NodeBuffer[y-1][x])
        if y < len(path) - 1:
          if path[y+1][x] != 2:
            succesors.append(NodeBuffer[y+1][x])

        NodeBuffer[y][x].succesors = succesors

# ------ Heuristicas ------
def _manhattan(arbol:Tree, actual:Node, last:Node) -> int:
  '''
  Heuristica 1: manhattan
  Devuelve la distancia aprximada entre el nodo actual y la meta
  '''
  distances = []
  for goal in arbol.goal:
    h = abs(actual.x - goal.x) + abs(goal.y - actual.y)
    distances.append(h)

  return min(distances)

def _diagnoal(arbol:Tree, actual:Node, last:Node):
  '''
  Heuristica 2: Distancia diagonal
  Devuelve la distancia diagonal entre el nodo actual y el nodo final
  '''
  hs = []
  for goal in arbol.goal:
    x = abs(actual.x - goal.x)
    y = abs(goal.y - actual.y)
    h = (x + y) - 1 * min(x, y)
    hs.append(h)
  
  return min(hs)


# ------ Clase de busqueda ------

from Framework import Framework

class AStar(Framework):
  def __init__(self, path) -> None:
    ''' Define los atributos iniciales y construye la instancia del algoritmo de búsqueda '''
    self.HEURISTIC = _manhattan
    self.GOAL = None
    self.arbol = Tree(path)
    self.open:list = [self.arbol.root]
    self.closed:list = []
    self.q:Node = self.arbol.root
    self.grid = path

  # ------ Metodos ------
  def goalTests(self) -> bool:
    return self.GOAL != None

  def setHeuristic(self):
    ''' Define la heuristica a utilizar '''
    if self.HEURISTIC == _manhattan: self.HEURISTIC = _diagnoal
    if self.HEURISTIC == _diagnoal: self.HEURISTIC = _manhattan

  def _qFinder(self):
    ''' Devuelve el nodo con menor f en la lista open '''
    initial_q = self.q
    for n in self.open:
      if n in self.q.succesors:
        self.q = n
        break

    for node in self.open:
      if (
        node.f < self.q.f 
        and node not in self.closed
        and node in initial_q.succesors
      ):
        self.q = node

  def _calculateG(self, actual:Node, last:Node) -> int:
    '''
    Calculo de parametro g
    costo del ultimo nodo visitado hacia el siguiente
    '''
    if actual.value == 2: return 9999999
    return abs(last.x - actual.x) + abs(actual.y - last.y)

  def stepCost(self, **kargs) -> int:
    '''
    Calcula el costo del siguiente paso (parametro f de un nodo)
    '''
    node = kargs['node']
    g = self._calculateG(node, self.q)
    h = self.HEURISTIC(self.arbol, node, self.q)
    return g + h

  def pathCost(self, s) -> int:
    ''' Devuelve el costo final del camino '''
    cost = len(self.closed)
    cost += 1 if self.GOAL != None else 0
    return cost 

  def action(self, s) -> str:
    '''
    Implementacion de algoritmo A*
    Referencia: https://www.geeksforgeeks.org/a-search-algorithm/
    '''
    if self.GOAL != None: return
    self._qFinder() # Escoje la q en la lista open con f mas bajo
    self.open.remove(self.q) # Quita el nodo q de la lista open

    # Se exploran todos los sucesores del nodo q
    for node in self.q.succesors:
      # Si el nodo objetivo es sucesor de q, se para la busqueda
      if node.value == 3:
        self.GOAL = node
        break

      # Se calcula f para el nodo actual
      actual_f = self.stepCost(node = node)

      '''
      Si el nodo esta en alguna de las listas: open y closed con un valor f menor al calculado en esta iteracion:
        Se ignora este nodo para esta iteracion
      sino:
        se asigna la f calculada al nodo actual
      '''
      if (
        (node in self.open and node.f < actual_f)
        or (node in self.closed and node.f < actual_f)
      ): continue
      
      node.f = actual_f

      # Si el nodo actual no esta en open ni closed, se agrega a open
      if (
        node not in self.open 
        and node not in self.closed
      ):
        self.open.append(node)

    # Se agrega q a closed ( es decir se agrega al camino recorrido )
    self.closed.append(self.q)

  def results(self, s, a) -> int:
    '''
    Devuelve el camino tomado hasta el momento de la ejecucion
    '''
    result = [(node.x, node.y) for node in self.closed]
    if self.GOAL != None:
      result.append((self.GOAL.x, self.GOAL.y))
    return result

  def results(self, s, a) -> int:
    '''
    Devuelve el grid con el camino tomada hasta el estado actual
    '''
    for node in self.closed:
      if self.grid[node.y][node.x] == 0:
        self.grid[node.y][node.x] = 4

    return self.grid


# ---------- Ejemplo de USO ----------

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


A_instance = AStar(path)

while not A_instance.goalTests():
  A_instance.action('')
  print('pathCost:', A_instance.pathCost(''))
  grid = A_instance.results('', '')
  for row in grid:
    print(row)
