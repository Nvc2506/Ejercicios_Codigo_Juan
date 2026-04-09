from abc import ABC, abstractmethod
from typing import Optional

class Movible(ABC):
    @abstractmethod
    def mover(self) -> None:
        pass

class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = ""
        self.nombre = nombre
    @property
    def nombre(self) ->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, valor:str) -> None:
        if isinstance(valor, str) and valor.strip():
            self.__nombre = valor.strip().title()
        else:
            raise ValueError (" El nombre debe ser una cadena de texto valido")
    @abstractmethod
    def sonido(self) -> None:
        pass
class Perro(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} (Perro) dice: Guuu Guauuu")
class Gato(Animal):
    def sonido(self) -> None:  
        print(f"{self.nombre} (Gato) dice: Miauu")
class Vaca(Animal):
    def sonido(self) -> None:
       print(f"{self.nombre} (Vaca) dice: Muuu")
class Leon(Animal, Movible):
    def sonido(self) -> None:
        print(f"{self.nombre} (Leon) dice: Roooarr")
    def mover(self) -> None:
        print(f"{self.nombre} Camila sigilisamente por la sabana...")
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()
def desplazar(animal: Movible) -> None:
    animal.mover()
    
def main():
    try:
        animales =[
            Perro("Rocky"),
            Gato("Misu"),
            Vaca("Lola"),
            Leon("Simba")
        ]
        print("** POLIFORMISMO EN MODELO ZOOLOGICO ===\n")
        for animal in animales:
            hacer_sonido(animal)
        print("\n Movimiento +++")
        for animal in animales:
            if isinstance(animal, Movible):
                desplazar(animal)
    except ValueError as  e:
        print(f"Error de validacion: {e}")
if __name__ =="__main__":
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        