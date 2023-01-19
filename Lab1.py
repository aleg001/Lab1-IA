"""
Lab#1


Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""


from PIL import Image
import numpy as np

# Constantes


Pixel = 20
path = "l1.bmp"
image = Image.open(path).convert("RGB")
imagenChiqui = image.resize((64, 64), Image.BILINEAR)
resultado = imagenChiqui.resize(image.size, Image.NEAREST)
resultado.save("resultado.bmp")


image = np.asarray(image)


class Imagen:
    def LectorImagen(imagen):
        informacion = imagen.load()
        altura = imagen.height
        ancho = imagen.width
        matrizResultante = []

        # PENDIENTE: llenar matriz


#  BFS
def BFS(problemFramework):
    Matriz = Imagen.LectorImagen(problemFramework)
    Siguiente = []

    while Siguiente is not None:
        print("Siguiente xd")
