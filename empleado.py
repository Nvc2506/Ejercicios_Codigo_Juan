class Empleado:
    def trabajar(self):
        print("el empleado realiza tareas de su contrato laboral")

class Gerente(Empleado):
    def trabajar(self):
        print("el gerente es el que lidera el equipo de trabajo")

def main():
    Empleado1 = Empleado()
    Empleado1.trabajar()
    print("Creo al gerente 1 y este ya sobreescribe el metodo trabajar del padre ")
    Gerente1 = Gerente()
    Gerente1.trabajar()

if __name__=="__main__":
    main()