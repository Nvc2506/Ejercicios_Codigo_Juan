from abc import ABC, abstractmethod

class Empleado(ABC):

    def __init__(self, nombre: str) -> None:
        self._nombre = None
        self._nombre = nombre 
        
        @property
        def nombre(self) -> str:
            return self._nombre
        
        @nombre.setter
        def nombre(self, valor: str) -> None:
            if isinstance(valor, str) and valor.strip() and valor != "":
                self._nombre = valor.strip()
            else:
                raise ValueError("El nombre debe ser un texto valido")
            
            @abstractmethod
            def trabajar(self) -> None:
                pass

class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta realizando la administracion de la empresa")

class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta programando una solucion en python")

def ejecutar_tarea(empleado : Empleado) -> None:
    empleado.trabajar()

def main():
    print("***** INICIO DEL PROGRAMA DE EMPLEADO EMPRESA SENA *****")
    desarrollador1 = Desarrollador("Alexander joaquin")
    gerente1 = Gerente("Juanito Perez")
    ejecutar_tarea(desarrollador1)
    ejecutar_tarea(gerente1)

if __name__ == "__main__":
    main()