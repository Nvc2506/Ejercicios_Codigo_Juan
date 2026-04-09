class Perro:
    def __init__(self, nombre, raza, color, tamaño, edad): 
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.tamaño = tamaño
        self.edad = edad
    def mostrar_info(self):
        print(f"Nombre del perro: {self.nombre}")
        print(f"La raza {self.raza}")
        print(f"El color {self.color}")
        print(f"el tamaño {self.tamaño}")
        print(f"la edad {self.edad}")
def main ():
    nombre = input(f"Ingrese el nombre del perro: ")
    raza = input (f"ingrese la raza del perro: ")
    color = input (f"Ingrese el color del perro: ")
    tamaño = input (f"Ingrese el tamaño del perro: ")
    edad = input (f"Ingrese la edad del perro: ")
    perro1 = Perro(nombre, raza, color, tamaño, edad)  
    perro1.mostrar_info()
if __name__ == "__main__":
    main()