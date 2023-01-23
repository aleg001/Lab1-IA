from abc import ABC, abstractmethod


class Framework(ABC):
    @abstractmethod
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def name(self) -> str:
        return self._name
