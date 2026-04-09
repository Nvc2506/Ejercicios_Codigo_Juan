from dataclasses import dataclass

@dataclass
class Cliente:
    nombre:str
    edad: int = 18 #se crea una constante

cliente1 = Cliente("Ana")
print (cliente1)


