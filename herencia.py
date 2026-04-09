
class Padre:
    def __init__(self,mensaje, color_ojos, tipo_sangre):
        self.mensaje = mensaje
        self.color_ojos = color_ojos
        self.tipo_sangre = tipo_sangre

class Hijo(Padre):
    def __init__(self, mensaje, nombre, color_ojos, tipo_sangre, genero, estatura):
        super().__init__(mensaje,color_ojos,tipo_sangre)
        self.nombre = nombre
        self.genero = genero
        self.estatura = estatura

def main():
    obj = Hijo("Hola desde la clase Padre"," Luis"," verdes"," o+"," Masculino"," 1,70")
    print(f"{obj.mensaje},{obj.nombre},{obj.color_ojos},{obj.tipo_sangre},{obj.genero},{obj.estatura}")

if __name__ == "__main__":
    main()

