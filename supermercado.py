class Estudiante:
    def __init__(self, nombre, documento, nota_parcial, nota_final):  #Nota parcial = 20% #Nota final = 50%
        self.nombre = nombre
        self.documento = documento
        self.nota_parcial = nota_parcial
        self.nota_final = nota_final
    def result(self):
        print(f"La nota final de los estudiantes es la siguiente:")
        
class presencial(Estudiante):
    def __init__(self, nombre, documento, nota_parcial, nota_final, nota_foro):
        super().__init__(nombre, documento, nota_parcial, nota_final)
        self.nota_foro = nota_foro
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Nota parcial: {self.nota_parcial}")
        print(f"Nota final: {self.nota_final}")
    def result(self):
        nota_total = (self.nota_parcial * 0.2) + \
        (self.nota_final * 0.5) + \
        (self.nota_foro * 0.3)
        return nota_total
    def resultado(self):
        print(f"La nota final es: {self.result():.1f}")
        
class investigacion(Estudiante):
    def __init__(self, nombre, documento, nota_parcial, nota_final, nota_proyecto):
        super().__init__(nombre, documento, nota_parcial, nota_final)
        self.nota_proyecto = nota_proyecto
    def mostrar_info(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Nota parcial: {self.nota_proyecto}")
        print(f"Nota final: {self.nota_final}")
    def result(self):
        nota_total = (self.nota_parcial * 0.2) + \
        (self.nota_final * 0.5) + \
        (self.nota_parcial * 0.3)
        return nota_total
    def resultado(self):
        print(f"La nota final es: {self.result():.1f}")

def main():
    presencial1 = presencial("Miguelin", "456123", 3.9, 4.5, 4.2)
    presencial1.mostrar_info()
    presencial1.resultado()
    investigacion1 = investigacion("Ardnold", "789654", 5, 2.3, 3.9)
    investigacion1.mostrar_info()
    investigacion1.resultado()
if __name__ == "__main__":
    main()