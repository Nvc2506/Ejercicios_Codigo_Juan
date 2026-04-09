class Aprendiz:
    def __init__(self, nombre, edad, peso, estatura):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__estatura = estatura

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_peso(self):
        return self.__peso
    
    def get_estatura(self):
        return self.__estatura
    
    
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

        if isinstance(nueva_edad, (int, float)) and nueva_edad >0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad debe ser valida")

    
    def set_peso(self, nuevo_peso):
        self.__peso = nuevo_peso


        if isinstance(nuevo_peso, (int, float)) and nuevo_peso >0:
            self.__peso = nuevo_peso
        else:
            raise ValueError("El peso debe ser valido")
        
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre} \n Edad actual: {self.__edad} \n Peso actual: {self.__peso} \n Estatura: {self.__estatura}")

def main():
    print("\n APRENDICES")
    aprendiz1 = Aprendiz("Miguel Gogo",18,55,1.63)
    aprendiz2 = Aprendiz("Aaron Quintana",20,65,1.78)
    aprendiz3 = Aprendiz("Niquito Velandia",17,78,1.72)

    print("Info adicional de los aprendices")
    aprendiz1.mostrar_info()
    aprendiz2.mostrar_info()
    aprendiz3.mostrar_info()
    
    
    print("Edad actual :", aprendiz1.get_edad() ,"\n ")
    print("Edad actual:", aprendiz2.get_edad())
    print("Edad actual:", aprendiz3.get_edad())
    aprendiz1.set_edad(21)
    aprendiz2.set_edad(18)
    aprendiz3.set_edad(19)

    print("Edad actual:", aprendiz1.get_edad())
    print("Edad actual:", aprendiz2.get_edad())
    print("Edad actual:", aprendiz3.get_edad())

    print("\n Programa finalizao.")    
if __name__ == "__main__":
    main()




        


