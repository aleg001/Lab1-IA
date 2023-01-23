"""
Lab#1

Módulo de procesamiento de imágenes
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""


from PIL import Image
import numpy as np

# Se importa libreria para volver imagenes a pixeles
from pixelate import *

# Constantes
Pixel = 20
path = "l1.bmp"
# Se llama a funcion de pixelate, recibiendo como parametro la imagen input, la imagen output y el tamaño de los pixeles.
pixelate(path, "l11.bmp", Pixel)
