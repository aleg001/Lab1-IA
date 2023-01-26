"""
Lab#1
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""
"""
Referencias:
https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
https://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image

"""
from PIL import Image
from ImageProcessing import *
from BMP_RW import *
from BFS import *
from DFS import *
from AStar import *
import math

print("Resultado: ")
Resultado = CargaImagenes("l1")

# Conversión de matriz de numpy a matrix con arrays
ResultadoTemp = []
raiz = int(math.sqrt(Resultado.size))
count = 0
for i in range(raiz):
    temp = []
    for j in range(raiz):
        temp.append(Resultado.item(count))
        count += 1
    ResultadoTemp.append(temp)

Resultado = ResultadoTemp

grid2 = []
cy = 0
block = 10
for y in range(int(raiz/block)):
    cx = 0
    temp_x = []
    for x in range(int(raiz/block)):
        temp_x.append(Resultado[cy][cx])
        cx += block
    grid2.append(temp_x)
    cy += block
        
Resultado = grid2
'''BFSTest = BFS(Resultado)
print(BFSTest.path)
# for i in BFSTest.MtoGtoM:
#     print(i)

print('gen info: ', BFSTest.inicio, BFSTest.fin)

print("step cost: ", BFSTest.stepCost())
print("path cost: ", BFSTest.pathCost(BFSTest.path))

s = (BFSTest.graph, BFSTest.inicio, BFSTest.fin, BFSTest.v, [0 for i in range(BFSTest.v)], [0 for i in range(BFSTest.v)])
print("Pass test: ", BFSTest.goalTests(s))
'''



import pygame

def draw_rect(x, y, color):
  '''Draws a cube of size blockize-1 in the grid'''
  screen.fill(
    color,
    (x*blocksize, H - y*blocksize, blocksize, blocksize)
  )  

def paint_grid():
  '''Re-paints the pixels of the grid that have changed'''
  for y in range(len(GRID)):
    for x in range(len(GRID)):
        if GRID[y][x] == 0:
            draw_rect(y, x, (255, 255, 255))
        elif GRID[y][x] == 1:
            draw_rect(y, x, (0, 255, 0))
        elif GRID[y][x] == 2:
            draw_rect(y, x, (0, 0, 0))
        elif GRID[y][x] == 3:
            draw_rect(y, x, (255, 0, 0))
        elif GRID[y][x] == 4:
            draw_rect(y, x, (255, 0, 255))
        elif GRID[y][x] == 4:
            draw_rect(y, x, (100, 50, 50))


# ---- Main ----
if __name__ == '__main__':
  W, H = (600, 600)
  blocksize = int(600 / len(Resultado))
  GRID = Resultado

  A_instance = AStar(Resultado)
  A_instance.setHeuristic()
  
  pygame.display.set_caption("John Conway's Game of Life")
  screen = pygame.display.set_mode((W, H))
  pygame.init()

  actualgrid, nextgrid = 0, 1
  running = True
  changes = []

  while running:
    if not A_instance.goalTests():
        A_instance.action('')
        GRID = A_instance.results('', '')

    # Paint_grid
    paint_grid()

    # Flip
    pygame.display.update()
    input()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False