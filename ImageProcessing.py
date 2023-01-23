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
Pixel = 15
path = "l1.bmp"
endResult = "result.bmp"
# Se llama a funcion de pixelate, recibiendo como parametro la imagen input, la imagen output y el tamaño de los pixeles.
pixelate(path, endResult, Pixel)

# La imagen resultado se vuelve a cargar
endResultOpened = Image.open(endResult)
# Se convierte en un array la imagen. Referencia: https://thecleverprogrammer.com/2021/06/08/convert-image-to-array-using-python/#:~:text=Converting%20an%20Image%20to%20Array,pip%20install%20Pillow
data = np.asarray(endResultOpened)
print(data)
