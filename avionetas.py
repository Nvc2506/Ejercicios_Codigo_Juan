class Avion:
    def __init__(self, tamaño, marca, aerolinea, estrato, fabricante, color, materiales ): 
        self.marca = marca
        self.aerolinea = aerolinea
        self.color = color
        self.tamaño = tamaño
        self.estrato = estrato
        self.fabricante = fabricante
        self.materiales = materiales
    def mostrar_info(self):
        print(f"La marca {self.marca}")
        print(f"Aerolinea {self.aerolinea}")
        print(f"El estrato{self.estrato}")
        print(f"El fabricante{self.fabricante}")
        print(f"El color {self.color}")
        print(f"Fabricante {self.fabricante}")
        print(f"tipo de material {self.materiales}")
class main:
    tamaño = input ("Ingrese el tamaño del avion: ")
    marca = input ("ingrese la marca del avion: ")
    aerolinea = input ("ingrese a que aerolinea pertenece el avion: ")
    estrato = input ("ingrese que estrato es el avion (clase baja, clase media, clase alta): ")
    fabricante = input ("Ingrese el fabricante del avion: ")
    color = input ("ingrese el color del avion: ")
    materiales = input ("Ingrese los materiales con que esta hecho el avion: ")
    avion1 = Avion(tamaño, marca, aerolinea, estrato, fabricante, color, materiales)
    avion1.mostrar_info ()
if __name__ == "__main__" :
    main ()