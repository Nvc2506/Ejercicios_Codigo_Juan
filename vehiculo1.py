class vehiculo():
    def mover(self):
        print("El vehiculo se esta moviendo")

class carro(vehiculo):
    def mover(self):
        print("El carro se esta conduciendo ")

class avion(vehiculo):
    def mover(self):
        print("El avion esta volando")

class submarino(vehiculo):
    def mover(self):
        print("El submarino esta navegando")

def main():
    vehiculo1 = vehiculo()
    vehiculo1.mover()

    carro1 = carro()
    carro1.mover()

    avion1 = avion()
    avion1.mover()

    submarino1 = submarino()
    submarino1.mover()

if __name__ ==  "__main__":
    main()