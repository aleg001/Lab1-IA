"""
Referencias:
https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
https://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image

"""

# ===============================================================
# CÓDIGO OBTENIDO DEL CURSO GRÁFICOS POR COMPUTADOR 2022
# AUTOR ORIGINAL: DENNIS ALDANA
# MODIFICACIONES POR: ALEJANDRO GÓMEZ, MARÍA ISABEL SOLANO, DIEGO CÓRDOVA
# ===============================================================

from PIL import Image
import struct


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

    # Pixel data (width x height x 3 pixels)
    for x in range(height):
        for y in range(width):
            f.write(pixels[x][y])
    f.close()


# Constantes de colores en una clase:
class Colores:
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)


# Se abre imagen y se define el tamaño:
imagen = Image.open("l1.bmp")
pixelesGrid = imagen.load()
ancho = imagen.size[0]
altura = imagen.size[1]

# Definicion de colores en una clase:
class PosicionesDisponibles:
    espaciosDisponibles = Colores.BLANCO
    puntoInicio = Colores.ROJO
    metaPuntos = Colores.VERDE
    espaciosNoDisponibles = Colores.NEGRO


# Lista vacia a llenar con puntos de meta:
# -- Se llena con tuplas de coordenadas
PuntosDeMeta = []
# Se usa una tupla para almacenar coordenadas de inicio
puntoRojo = ()


for i in range(0, ancho):
    for j in range(0, altura):
        match pixelesGrid[i, j]:
            case PosicionesDisponibles.metaPuntos:
                PuntosDeMeta.append((i, j))
            case PosicionesDisponibles.puntoInicio:
                puntoRojo = (i, j)


# Funcion para detectar paredes (ver si la posicion si es valida)
def detectarParedes(x, y, w, h):
    match pixelesGrid[x, y]:
        case PosicionesDisponibles.espaciosDisponibles:
            return True
        case PosicionesDisponibles.espaciosNoDisponibles:
            return False
        case PosicionesDisponibles.puntoInicio:
            return True
        case PosicionesDisponibles.metaPuntos:
            return True
