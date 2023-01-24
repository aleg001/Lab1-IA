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

# Se importa clase de colores
from Colores import *

# Constantes
Pixel = 15
path = "l1.bmp"
endResult = "result.bmp"
# Se llama a funcion de pixelate, recibiendo como parametro la imagen input, la imagen output y el tamaño de los pixeles.
pixelate(path, endResult, Pixel)

# Se define paleta de colores
colores = [Colores.ROJO, Colores.VERDE, Colores.NEGRO, Colores.BLANCO]

# La imagen resultado se carga
endResultOpened = Image.open(endResult)
# Se cambia a paleta de colores y se cuantiza a estos
imagen = endResultOpened.convert("RGB", palette=colores)
im1 = endResultOpened.quantize(4)

# Se obtiene la información de la imagen
informacionFoto = endResultOpened.getdata()
imagen4Colores = []


# Se reduce a 4 colores la imagen
index = 0
# Se itera sobre la cantidad de pixeles
while index < len(informacionFoto):
    item = informacionFoto[index]
    # Se chequea el rango rgb 0,200 para saber si es negro segun el pixel
    if all(0 <= x <= 200 for x in item):
        imagen4Colores.append(Colores.NEGRO)
    # Se chequea el rango rgb 100,120 para saber si es rojo segun el pixel
    elif all(100 <= x <= 120 for x in item):
        imagen4Colores.append(Colores.ROJO)
    # Se chequea el rango rgb 150,170 para saber si es verde segun el pixel
    elif all(150 <= x <= 170 for x in item):
        imagen4Colores.append(Colores.VERDE)
    # Se chequea el rango rgb 200,255 para saber si es blanco segun el pixel
    elif all(200 <= x <= 255 for x in item):
        imagen4Colores.append(Colores.BLANCO)
    else:
        imagen4Colores.append(item)
    # Se sigue al siguiente pixel
    index += 1

# Se agrega la data a la imagen
endResultOpened.putdata(imagen4Colores)
# Se despliega imagen
endResultOpened.show()
# Se guarda imagen
endResultOpened.save(endResult)

# Se convierte en un array la imagen. Referencia: https://thecleverprogrammer.com/2021/06/08/convert-image-to-array-using-python/#:~:text=Converting%20an%20Image%20to%20Array,pip%20install%20Pillow
data = np.asarray(endResultOpened)
print(data)
