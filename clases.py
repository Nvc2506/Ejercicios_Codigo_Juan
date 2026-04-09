
class Empleado: 
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} esta realizando un trabajo de la empresa")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    def mostar_info(self):
        print(f"nombre: Atributo del padre: {self.nombre}")
        print(f"salario: Atributo del padre: {self.salario}")
        print(f"departamento: Atributo del Hijo: {self.departamento}")

class Vendedor(Empleado):
    def __init__(self, nombre, salario, ciudad, comision):
        super().__init__(nombre, salario)
        self.ciudad = ciudad
        self.comision = comision
    def mostrar_info(self):
        print(f"nombre: Atributo del padre: {self.nombre}")
        print(f"salario: Atributos del padre: {self.salario}")
        print(f"ciudad:{self.ciudad}")
        print(f"comision:{self.comision}")

def main():
    Gerente1 = Gerente("Carlos",2340000,"software")
    Gerente1.mostar_info()
    Vendedor1 = Vendedor("Sapo", 567000,"cauca","50%")
    Vendedor1.mostrar_info()

if __name__ == "__main__":
    main()

