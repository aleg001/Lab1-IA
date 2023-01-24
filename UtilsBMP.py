from PIL import Image

import numpy


"""
Función que pasa un array
a un archivo BMP, usando PIL y numpy
"""


def writeBMP(array, nombreArchivo):
    imagen = Image.fromarray(numpy.uint8(array))
    imagen.save(nombreArchivo + ".bmp")


"""
Función que abre un BMP y 
lo convierte en un array
"""


def readBMP(filepath):
    img = Image.open(filepath)
    width, height = img.size
    pixels = numpy.array(img)
    return width, height, pixels
