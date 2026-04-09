class Aprendiz:
    def __init__(self, nombre, documento, edad, peso, estatura, genero):
        self.nombre = nombre
        self.documento = documento
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.genero = genero

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Estatura: {self.estatura} m")
        print(f"Género: {self.genero}")
        print("---------------------------")


# Crear lista de 6 aprendices
aprendices = [
    Aprendiz("Yesu", "123", 18, 60, 1.65, "F"),
    Aprendiz("Juan", "456", 20, 70, 1.75, "M"),
    Aprendiz("Ana", "789", 19, 55, 1.60, "F"),
    Aprendiz("Luis", "321", 22, 80, 1.80, "M"),
    Aprendiz("Sofia", "654", 21, 58, 1.62, "F"),
    Aprendiz("Carlos", "987", 23, 85, 1.78, "M")
]

# 🔹 Mostrar toda la información organizada
print("\n=== INFORMACIÓN DE APRENDICES ===")
for a in aprendices:
    a.mostrar_info()

# 🔹 Mostrar solo nombres
print("\n=== NOMBRES ===")
for a in aprendices:
    print(a.nombre)

# 🔹 Mostrar nombre y género
print("\n=== NOMBRE Y GÉNERO ===")
for a in aprendices:
    print(f"{a.nombre} - {a.genero}")