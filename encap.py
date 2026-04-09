class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo       #Atributo privado
        self.__precio = precio       #

#Getter permite acceder al valor de forma segura
    def get_precio(self):
        return self.__precio
    
    def get_titulo(self):
        return self.__titulo
    
#Setter controla y valida antes de modificar el valor
    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser un numero valido")
        
#Metodo adicional para visualizar los datos del libro
    def mostrar_info(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Precio actual: ${self.__precio:,.2f}")
def main():
    print("\n=== LIBROS PRO ===")
    libro1 = Libro("Python", 55000)
    libro2 = Libro("Java", 120000)

    print("Info adicional del libro")
    libro1.mostrar_info()
    libro2.mostrar_info()

    print("Precio actual:", libro1.get_precio())
    print("Precio actual:", libro2.get_precio())
    libro1.set_precio(45000)
    libro2.set_precio(220000)
    
    print("Precio actual:", libro1.get_precio())
    print("Precio actual:", libro2.get_precio())
    
    print("\n Programa finalizado.")
if __name__ == "__main__":
    main()
