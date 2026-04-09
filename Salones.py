class Ambiente:
    def __init__(self, codigo, nombre, resposanble, puestos):
        self.codigo = codigo
        self.nombre = nombre
        self.responsable = resposanble
        self.puestos = puestos

ambiente1 = Ambiente(218, "Sistemas", "Juan Carlos", 30)
ambiente2 = Ambiente(220, "Ingles", "Manuel Beltran", 28)
ambiente3 = Ambiente(231, "Quimica", "Valeria Correa", 25)
ambiente4 = Ambiente(225, "TIC", "Belman", 30)


print("Informacion de los ambientes \n")
print(f"Primer ambiente: \n Codigo: {ambiente1.codigo} \n Nombre: {ambiente1.nombre} \n Responsable: {ambiente1.responsable} \n Puestos: {ambiente1.puestos}")
print(f"Seggundo ambiente: \n Codigo: {ambiente2.codigo} \n Nombre: {ambiente2.nombre} \n Responsable: {ambiente2.responsable} \n Puestos: {ambiente2.puestos}")
print(f"Tercer ambiente: \n Codigo: {ambiente3.codigo} \n Nombre: {ambiente3.nombre} \n Responsable: {ambiente3.responsable} \n Puestos: {ambiente3.puestos}")
print(f"Cuarto ambiente: \n Codigo: {ambiente4.codigo} \n Nombre: {ambiente4.nombre} \n Responsable: {ambiente4.responsable} \n Puestos: {ambiente4.puestos}")

