from PIL import Image

import numpy


"""
Función que pasa un array
a un archivo BMP, usando PIL y numpy
"""


def ArrayNPBMP(array, nombreArchivo):
    imagen = Image.fromarray(numpy.uint8(array))
    imagen.save(nombreArchivo + ".bmp")
