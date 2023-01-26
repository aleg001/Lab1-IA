"""
Lab#1
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""
import time


def maquinaEscribir(mensajito: str):
    for i in mensajito:
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()


maquinaEscribir("Bienvenido al Laboratorio#1 de IA")


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
    elif choice == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
