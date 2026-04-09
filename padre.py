class Padre:
    def __init__(self, mensaje):
        self.mensaje = mensaje

class Hijo(Padre):
    def __init__(self, mensaje, nombre):
        super().__init__(mensaje)
        self.nombre = nombre

def main():
    Padre1 = Padre("Soy el papa")
    print(Padre1.mensaje)
    Hijo1 = Hijo("Soy el hijo y utilizo la variable del padre", "Jose")
    print(Hijo1.mensaje)
    print(Hijo1.nombre)

if __name__ == "__main__":
    main()