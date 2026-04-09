"""class Operacion():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        print("***** ALERTA vamos a iniciar operacion ATENTOS *****")

class Suma(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("preparando la operacion SUMA")

    def calcular(self):
        super().calcular()
        resultado = self.numero1 + self.numero2
        print(f"el resultado de la suma es: {resultado}")

        resultado = self.numero1 - self.numero2
        print(f"el resultado de la resta es: {resultado}")

        resultado = self.numero1 * self.numero2
        print(f"el resultado de la multiplicacion es: {resultado}")

        resultado = self.numero1 / self.numero2
        print(f"el resultado de la division es: {resultado}")

        resultado = self.numero1 ** self.numero2
        print(f"el resultado de la potencia es: {resultado}")

def main():
    operacion1 = Suma(20, 30)
    operacion1.calcular()

    operacion2 = Suma(10, 30)
    operacion2.calcular()

    operacion3 = Suma(5, 5)
    operacion3.calcular()

    operacion4 = Suma(30, 19)
    operacion4.calcular()

    operacion5 = Suma(30, 50)
    operacion5.calcular()
    print("YA PASO LA ALERTA FIN DEL ALGORITMO")


if __name__ == "__main__":
    main()"""

class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def validar(self):
        if not isinstance(self.a, (int,float)) or not isinstance(self.b, (int,float)):
            raise ValueError("los valores deben ser numericos") 
    
    def mostar_datos(self):
        print(f"los datos proporcionados son: {self.a} y {self.b}")

    def calcular(self):
        print("** REALIZANDO LA OPERACION MATEMATICA **")

class Suma(Operacion):
    def calcular(self):
        super().validar()
        super().mostar_datos()
        super().calcular()
        resultado = self.a + self.b
        print(f"el resultado de la operacion SUMA es: {resultado}")

class Resta(Operacion):
    def calcular(self):
        super().validar()
        super().mostar_datos()
        super().calcular()
        resultado = self.a - self.b
        print(f"el resultado de la operacion RESTA es: {resultado}")

class Multiplicacion(Operacion):
    def calcular(self):
        super().validar()
        super().mostar_datos()
        super().calcular()        
        resultado = self.a * self.b
        print(f"el resultado de la operacion MULTIPLICACION es: {resultado}")

class Division(Operacion):
    def calcular(self):
        super().validar()
        super().mostar_datos()
        super().calcular()
        if self.b and self.a == 0:
            print("no se puede dividir entre 0")
        else:
            resultado = self.a / self.b
            print(f"el resultado de la operacion DIVISION es: {resultado}")

class Potencia(Operacion):
    def calcular(self):
        super().validar()
        super().mostar_datos()
        super().calcular()
        if self.b > 3:
            print("el segundo numero no puede ser mayor a 3")
        else:
            resultado = self.a ** self.b
            print(f"el resultado de la operacion POTENCIA es: {resultado}")

def main():
    print("OPERACION SUMA")
    operacion1 = Suma(32, 54)
    operacion1.calcular()

    print("OPERACION RESTA")
    operacion2 = Resta(32, 54)
    operacion2.calcular()

    print("OPERACION MULTIPLICACION")
    operacion3 = Multiplicacion(32, 54)
    operacion3.calcular()

    print("OPERACION DIVISION")
    operacion4 = Division(5, 10)
    operacion4.calcular()

    print("OPERACION POTENCIA")
    operacion5 = Potencia(4, 5)
    operacion5.calcular()

if __name__ == "__main__":
    main()
