"""
Lab#1
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""
from PIL import Image
import struct
import numpy

# ===============================================================
# CÓDIGO OBTENIDO DEL CURSO GRÁFICOS POR COMPUTADOR 2022
# AUTOR ORIGINAL: DENNIS ALDANA
# MODIFICACIONES POR: ALEJANDRO GÓMEZ, MARÍA ISABEL SOLANO, DIEGO CÓRDOVA
# ===============================================================


def char(c):
    """
    Input: requires a size 1 string
    Output: 1 byte of the ascii encoded char
    """
    return struct.pack("=c", c.encode("ascii"))


def word(w):
    """
    Input: requires a number such that (-0x7fff - 1) <= number <= 0x7fff
           ie. (-32768, 32767)
    Output: 2 bytes
    Example:
    >>> struct.pack('=h', 1)
    b'\x01\x00'
    """
    return struct.pack("=h", w)


def dword(d):
    """
    Input: requires a number such that -2147483648 <= number <= 2147483647
    Output: 4 bytes
    Example:
    >>> struct.pack('=l', 1)
    b'\x01\x00\x00\x00'
    """
    return struct.pack("=l", d)


def color(r, g, b):
    """
    Input: each parameter must be a number such that 0 <= number <= 255
           each number represents a color in rgb
    Output: 3 bytes
    Example:
    >>> bytes([0, 0, 255])
    b'\x00\x00\xff'
    """
    return bytes([b, g, r])


# ===============================================================
# BMP
# ===============================================================

"""
Función que pasa un array
a un archivo BMP, usando PIL y numpy
"""


def writebmp(filename, width, height, pixels):
    f = open(filename, "bw")

    # File header (14 bytes)
    f.write(char("B"))
    f.write(char("M"))
    f.write(dword(14 + 40 + width * height * 3))
    f.write(dword(0))
    f.write(dword(14 + 40))

    # Image header (40 bytes)
    f.write(dword(40))
    f.write(dword(width))
    f.write(dword(height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(width * height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    for x in range(height):
        for y in range(width):
            f.write(pixels[x][y])
    f.close()

    return filename


"""
Función que abre un BMP y 
lo convierte en un array
"""


def readBMP(filepath):
    img = Image.open(filepath)
    width, height = img.size
    pixels = numpy.array(img)
    return width, height, pixels
