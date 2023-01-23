"""
Lab#1

Implementacion de algoritmo A*
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""

from math import sqrt
from cmath import pi

# ------ Arbol ------
class Node:
  def __init__(self, x, y, value) -> None:
    self.f = 0
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

# ------ Clase de busqueda ------

# TODO implementar framework y hacer framework xd
class AStar(object):
  def __init__(self, path) -> None:
    ''' Define los atributos iniciales y construye la instancia del algoritmo de búsqueda '''
    self.HEURISTIC = self._manhattan
    self.GOAL = None
    self.arbol = Tree(path)

  # ------ Heuristicas ------
  def _manhattan(self, arbol:Tree, actual:Node, last:Node) -> int:
    '''
    Heuristica 1: manhattan
    Devuelve la distancia aprximada entre el nodo actual y la meta
    '''
    distances = []
    for goal in arbol.goal:
      h = abs(actual.x - goal.x) + abs(goal.y - actual.y)
      distances.append(h)

    return min(distances)

  #
  def _diagnoal(self, arbol:Tree, actual:Node, last:Node):
    hs = []

    for goal in arbol.goal:
      x = abs(actual.x - goal.x)
      y = abs(goal.y - actual.y)
      d2 = sqrt(2)
      h = (x + y) + (d2 - 2) * min(x, y)
      hs.append(h)
    
    return min(hs)

  # ------ Metodos ------

  def setHeuristic(self):
    ''' Define la heuristica a utilizar '''
    if self.HEURISTIC == self._manhattan: self.HEURISTIC = self._diagnoal
    if self.HEURISTIC == self._diagnoal: self.HEURISTIC = self._manhattan

  def _qFinder(self, open:list[Node], closed: list[Node], q:Node):
    ''' Devuelve el nodo con menor f en la lista open '''
    initial_q = q
    for n in open:
      if n in q.succesors:
        q = n
        break

    for node in open:
      if (
        node.f < q.f 
        and node not in closed
        and node in initial_q.succesors
      ):
        q = node

    return q

  def _calculateG(self, actual:Node, last:Node) -> int:
    '''
    Calculo de parametro g
    costo del ultimo nodo visitado hacia el siguiente
    '''
    if actual.value == 2: return 9999999
    return abs(last.x - actual.x) + abs(actual.y - last.y)

  def starSearch(self, grid):
    open:list = [self.arbol.root]
    closed:list = []
    notGoal = True
    q:Node = self.arbol.root

    while len(open) > 0 and notGoal:
      q = self._qFinder(open, closed, q)
      open.remove(q)

      for node in q.succesors:
        if node.value == 3:
          notGoal = False
          break

        g = self._calculateG(node, q)
        h = self.HEURISTIC(self.arbol, node, q)
        node.f = g + h
        ignoreNode = False

        for n in open:
          if (
            n.x == node.x 
            and n.y == node.y
            and n.f < node.f
          ): 
            ignoreNode = True
            break
        
        if ignoreNode: continue

        for n in closed:
          if (
            n.x == node.x 
            and n.y == node.y
            and n.f < node.f
          ): 
            ignoreNode = True
            break

        if ignoreNode: continue
        if node not in open and node not in closed:
          open.append(node)
      closed.append(q)

    return [(node.x, node.y) for node in closed]


# pruebas ----------------------------------------------------------------------
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

path = [
  [0, 0, 0, 0],
  [0, 1, 2, 0],
  [2, 2, 2, 0],
  [0, 0, 0, 3],
]

A_instance = AStar(path)
# A_instance.setHeuristic()
res = A_instance.starSearch(path)
print(res)

