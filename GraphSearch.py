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
        count + 1
    ResultadoTemp.append(temp)

Resultado = ResultadoTemp

BFSTest = BFS(Resultado)
print(BFSTest.path)
# for i in BFSTest.MtoGtoM:
#     print(i)

# print("step cost: ", BFSTest.stepCost())
print("path cost: ", BFSTest.pathCost(BFSTest.path))

s = (BFSTest.graph, BFSTest.inicio, BFSTest.fin, BFSTest.v, [0 for i in range(BFSTest.v)], [0 for i in range(BFSTest.v)])
print("Pass test: ", BFSTest.goalTests(s))
