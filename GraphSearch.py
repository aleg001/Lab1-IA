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
from Vistas import *


def GraphSearch(laberinto):
    Resultado = CargaImagenes(laberinto)

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

    block = 0
    for row in Resultado:
        if 1 in row:
            block = row.count(1)
            break

    grid2 = []
    cy = 0
    for y in range(int(raiz / block)):
        cx = 0
        temp_x = []
        for x in range(int(raiz / block)):
            temp_x.append(Resultado[cy][cx])
            cx += block
        grid2.append(temp_x)
        cy += block

    Resultado = grid2
    return Resultado
