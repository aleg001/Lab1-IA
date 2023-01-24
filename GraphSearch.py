from PIL import Image
import queue


def EspacioBlanco(coordenada, imagen):

    listaconEspacios = []
    imageCoords = True
    for i in range(0, 3):
        if imagen[coordenada[i][0]][coordenada[i][1]] == 0:
            listaconEspacios.append(coordenada[i])
        if not imageCoords:
            break
        imageCoords = imagen[coordenada[1]][coordenada[0] * 3 + i] > 240
        return imageCoords


def BFS(s, e, i, visitados):
    frontera = queue.Queue()
