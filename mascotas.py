class Animales:
    def sonido(self):
        print("el animal hace un sonido")

class Gato(Animales):
    def sonido(self):
        print("el gato esta maullando")

class Perro(Animales):
    def sonido(self):
        print("el perro esta ladrando")

class Leon(Animales):
    def sonido(self):
        print("el leon esta rugiendo")

class Aguila(Animales):
    def sonido(self):
        print("el aguila esta chillando")

def main():
    Gato1 = Gato()
    Gato1.sonido()

    Perro1 = Perro()
    Perro1.sonido()

    Leon1 = Leon()
    Leon1.sonido()

    Aguila1 = Aguila()
    Aguila1.sonido() 


if __name__=="__main__":
    main()