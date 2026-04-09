from abc import ABC, abstractmethod

# Crearemos la clase abstracta, CLASE PADRE

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        print("***** CALCULAR AREA DEL CIRCULO *****")
        return 3.1416 * (self.radio **2)

class Cuadrado(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def calcular_area(self):
        print("***** CALCULAR AREA DE UN CUADRADO *****")
        return (self.lado1 * self.lado2)

class Triangulo(Figura):
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        print("***** CAlCULAR AREA DEL TRIANGULO *****")
        return (self.base * self.altura)

class Rectangulo(Figura):
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        print("***** CAlCULAR AREA DEL UN RECTANGULO *****")
        return (self.base * self.altura)

class Cubo(Figura):
    def __init__(self, arista):
        self.arista = arista
    def calcular_area(self):
        print("***** CALCULAR AREA DE UN CUBO *****")
        return 6 * (self.arista)

def mostrar_area(figura: Figura):
# Este metodo recibe cualquier objeto que sea de tipo figura
    print(f"El area: {figura.calcular_area():,.2f}")

def main():
    circulo1 = Circulo(8)
    mostrar_area(circulo1)

    cuadrado1 = Cuadrado(10,10)
    mostrar_area(cuadrado1)

    triangulo1 = Triangulo(23,12)
    mostrar_area(triangulo1)

    rectangulo1 = Rectangulo(30,25)
    mostrar_area(rectangulo1)

    cubo1 = Cubo(7)
    mostrar_area(cubo1)

    

if __name__ == "__main__":
    main()


