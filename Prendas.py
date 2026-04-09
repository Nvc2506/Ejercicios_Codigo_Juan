 # Clase Prenda
class Prenda:
    def __init__(self, codigo, nombre, responsable, precio, stock, color, ubicacion):
        self.codigo = codigo
        self.nombre = nombre
        self.responsable = responsable
        self.precio = precio
        self.stock = stock
        self.color = color
        self.ubicacion = ubicacion

    def mostrar_info(self):
        print("\n--- Información de la Prenda ---")
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Responsable:", self.responsable)
        print("Precio:", self.precio)
        print("Stock:", self.stock)
        print("Color:", self.color)
        print("Ubicación:", self.ubicacion)

    def modificar(self):
        print("\n¿Qué deseas modificar?")
        print("1. Precio")
        print("2. Stock")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nuevo_precio = float(input("Nuevo precio: "))
            self.precio = nuevo_precio
        elif opcion == "2":
            nuevo_stock = int(input("Nuevo stock: "))
            self.stock = nuevo_stock
        else:
            print("Opción no válida")


# Crear 4 objetos
prenda1 = Prenda("001", "Camisa", "Ana", 50000, 10, "Rojo", "A1")
prenda2 = Prenda("002", "Pantalón", "Luis", 80000, 5, "Azul", "B2")
prenda3 = Prenda("003", "Chaqueta", "Sofía", 120000, 3, "Negro", "C3")
prenda4 = Prenda("004", "Vestido", "Carlos", 95000, 7, "Blanco", "D4")

# Lista de prendas
prendas = [prenda1, prenda2, prenda3, prenda4]

# Menú
while True:
    print("\n--- SISTEMA DE PRENDAS ---")
    print("1. Mostrar prendas")
    print("2. Modificar prenda")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        for p in prendas:
            p.mostrar_info()

    elif opcion == "2":
        codigo = input("Ingresa el código de la prenda: ")
        for p in prendas:
            if p.codigo == codigo:
                p.modificar()
                break
        else:
            print("Prenda no encontrada")

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")