class Empleado:
    def __init__(self, nombre: str):

        if not Empleado.validar_nombre(nombre):
            raise ValueError("El nombre debe ser un texto valido")
        self.nombre = nombre

    def trabajar(self) -> None:
        print(f"{self.nombre} Esta realizando tareas generales")
  
    @staticmethod
    def validad_nombre(nombre: str) -> bool:
        return isinstance(nombre, str) and nombre.strip() != ""
    
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta coordinando el quipo y gestionando proyectos")

class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta escribiendo codigo")
def ejecutar_tarea(empleado: Empleado) -> None:
    empleado.trabajar()

def main() -> None:
    print("Es validado '' ?  ->", Empleado.validar_nombre("eduardo"))
    print("¿Es valido '' ? ->", Empleado.validar_nombre(""))
    gerente = Gerente("sofia")
    desarrollador = Desarrollador("jose")
    ejecutar_tarea(gerente)
    ejecutar_tarea(desarrollador)

if __name__ == "__main__":
    main()