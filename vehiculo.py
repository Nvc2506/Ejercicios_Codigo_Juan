# CLASE PADRE
class vehiculo:
    def mover(self):
        print("El vehiculo se mueve")

# CLASE HIJO
class carro(vehiculo):
    pass 


def main():
    vehiculo1 = vehiculo()
    vehiculo1.mover()
    carro1 = carro()
    print("# el carro hereda el metodo del vehiculo #")
    carro1.mover()
    
if __name__=="__main__":
    main()