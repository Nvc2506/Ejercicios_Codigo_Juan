class Automovil:
    def __init__(self, marca, modelo, color): #Constructor
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def mostrar_info(self):
        print(f"La marca del vehiculo: {self.marca}")
        print(f"El modelo del vehiculo: {self.modelo}")
        print(f"El color de del vehiculo: {self.color}")
def main():
        marca = input(f"Ingrese la marca del vehiculo: ")
        modelo = input (f"Ingrese el modelo del vehiculo: ")
        color = input (f"Ingrese el color del vehiculo: ")
        vehiculo1 = Automovil(marca, modelo, color)  # Utilizo el ingreso de los atributos  uno a uno
        vehiculo2 = Automovil("Camaro", 2027, "rojo")# Ingreso los datos directamente
        vehiculo1.mostrar_info()# Objeto 1
        vehiculo2.mostrar_info()# Objeto 2
if __name__ == "__main__":
        main()
#Crear una clase para los objetos, perro con al menos 5 atributos
# crear una clase para los objetos, avion, con almenos 7 atributos
# Crear clase clientes con 10 atributos 
