from abc import ABC, abstractmethod

# VAMOS A CREAR UNA CLASE ABSTRACTA

class Figura(ABC):
    @abstractmethod
# METODO ES OBLIGATORIO PARA TODAS LAS SUBCLASES
    def calcular_area(self):
        pass

# CREACION DE UNA CLASE NORMAL Y SE INVOCA LA ABC

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio **2)
    
class Cuadrado(Figura):
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura)
    
# CREAREMOS LA FUNCION QUE UTILIZARA POLIMORFISMO

def mostrar_area(figura: Figura):
    print(f"Area: {figura.calcular_area():,.2f}")

def main():
    # CREACION DEL OBJETO
    circulo = Circulo(5)
    # POLIMORFISMO PURO
    mostrar_area(circulo)

    cuadrado = Cuadrado(10, 5)
    mostrar_area(cuadrado)

if __name__ == "__main__":
    main()