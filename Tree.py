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
  def __init__(self, path:list[list]) -> None:
    for row in path:
      if 1 in row:
        self.root = Node(row.index(1), path.index(row), value = 1)

    NodeBuffer = [[] for y in range(len(path))]

    for y in range(len(path)):
      for x in range(len(path)):
        NodeBuffer[y].append(Node(x, y, path[y][x]))

    for y in range(len(path)):
      for x in range(len(path)):
        succesors = []
        succesors.append(NodeBuffer[y][x+1]) if x < len(path) else ''
        succesors.append(NodeBuffer[y][x-1]) if x > 0 else ''
        succesors.append(NodeBuffer[y+1][x+1]) if x < len(path) and x < len(path) else ''
        succesors.append(NodeBuffer[y+1][x-1]) if x > 0 and y < len(path) else ''
        succesors.append(NodeBuffer[y-1][x+1]) if y > 0 and x < len(path) else ''
        succesors.append(NodeBuffer[y-1][x-1]) if x > 0 and y > 0 else ''
        succesors.append(NodeBuffer[y-1][x]) if y > 0 else ''
        succesors.append(NodeBuffer[y-1][x]) if y < len(path) else ''

        NodeBuffer[y][x].succesors = succesors