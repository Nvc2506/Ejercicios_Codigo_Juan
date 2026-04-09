# Va a ser la clase padre

class vehiculo:         
    def mover(self):
        print("El vehiculo se esta moviendo")

# Va a ser la clase hija

class carro(vehiculo):          # Va a heredar el metodo mover de la clase padre osea de vehiculo
    pass
        
class moto(vehiculo):
    pass

def main():
    # Creare mi primer OBJETO
    vehiculo1 = vehiculo()
    vehiculo1.mover()

    # creare mi primer OBJRTO clase hijo
    print("la clase hijo CARRO repetira el metodo mover() de la clase padre")
    carro1 = carro()
    carro1.mover()

    print("la clase hijo MOTO repetira el metodo mover() de la calse padre")
    moto1 = moto()
    moto1.mover()

    print("la clase hijo avion")
    avion1 = vehiculo()
    avion1.volar()

if __name__ == "__main__":
    main()