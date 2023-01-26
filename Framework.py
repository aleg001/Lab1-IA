"""
Lab#1
------------------------------------
Alejandro Gomez
Maria Isabel Solano
Diego Cordova

"""
from abc import ABC, abstractmethod


class Framework(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # Función de acción actions(s) →  {a1, a2,...,an}
    @abstractmethod
    def action(self, s) -> str:
        pass

    # Función de resultados results(s,a) → s
    @abstractmethod
    def results(self, s, a) -> int:
        """Devuelve Array de nodos visitados en el estado actual"""
        pass

    # Función de goalTest(s) → {True, False}
    @abstractmethod
    def goalTests(self, s) -> bool:
        pass

    # Función de costo de paso stepCost(s,a,s) → R
    @abstractmethod
    def stepCost(self, **kargs) -> int:
        pass

    # Función de costo de ruta pathCost(s1, s2,...,sn) → R
    @abstractmethod
    def pathCost(self, s) -> int:
        pass
