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

print("Resultado: ")
Resultado = CargaImagenes("l1")
print(Resultado)

BFSTest = BFS(Resultado)
print(BFSTest.path)
for i in BFSTest.MtoGtoM:
    print(i)

print("step cost: ", BFSTest.stepCost())
print("path cost: ", BFSTest.pathCost(BFSTest.path))

print("Pass test: ", BFSTest.test)
