"""
Lab#1
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""
import time
from PIL import Image
from ImageProcessing import *
from BMP_RW import *
from BFS import *
from DFS import *
from AStar import *
from GraphSearch import *


def maquinaEscribir(mensajito: str):
    for i in mensajito:
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()


maquinaEscribir("Bienvenido al Laboratorio#1 de IA")


def SeleccionLaberinto():
    print("Seleccione una opción:")
    print("1. Laberinto #1")
    print("2. Laberinto #2")
    print("3. Laberinto #3")
    print("4. Laberinto #4")
    print("5. Otro")
    print("6. Salir")
    choice1 = input("Ingrese su opción: ")
    return choice1


def menu():
    print("Seleccione una opción:")
    print("1. BFS")
    print("2. DFS")
    print("3. AStar")
    print("4. Exit")
    choice = input("Ingrese su opción: ")
    return choice


while True:
    choice = menu()
    if choice == "1":
        print("Ejecutando BFS...")
    elif choice == "2":
        print("Ejecutando DFS...")
    elif choice == "3":
        print("Ejecutando AStar...")
        # La funcion de abajo corre el algoritmo con A*
        runAstar(GraphSearch("l1"))
    elif choice == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
