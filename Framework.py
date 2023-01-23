from typing import TypeVar, Generic
from abc import ABC

T = TypeVar("T")


class Framework(Generic[T], ABC):
    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        return self._name
