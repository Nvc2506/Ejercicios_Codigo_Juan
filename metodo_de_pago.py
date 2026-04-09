
from abc import ABC, abstractmethod
from typing import Optional

class Movible(ABC):
    @abstractmethod
    def mover(self) -> None:
        pass

class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre: str = ""
        self.nombre = nombre
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip().title()
        else:
            raise ValueError("El nombre debe ser una cadena de texto valida")
    @abstractmethod
    def sonido (self) -> None:
        pass
#crear calses hijas
class Perro(Animal):
    def sonido(self) -> None:
        pass
class Gato(Animal):
    def sonido(self) -> None:
        pass
class Vaca(Animal):
    def sonido(self) -> None:
        pass
#*******************************************
class Leon(Animal, Movible):
    def sonido(self) -> None:
        pass
    def mover(self) -> None:
        pass


