class Libro:
    def __init__(self, codigo, nombre_libro, autor, precio): #Constructor
        self.codigo = codigo
        self.nombre_libro = nombre_libro
        self.autor = autor
        self.precio = precio
mi_libro1 = Libro("ABC123","Don Quijote", "Miguel Cervantes", 80000)

print(mi_libro1.precio)
print(mi_libro1.autor)
print(mi_libro1.nombre_libro)
print(mi_libro1.codigo)

print(f"El precio del libro 1 es: {mi_libro1.precio}")
print(f"El autor del libro 1 es: {mi_libro1.autor}")
print(f"el nombre del libro es: {mi_libro1.nombre_libro}")
print(f"El codigo del libro es: {mi_libro1.codigo}")

mi_libro1.precio = 190000
print(f"El precio del libro 1 es: {mi_libro1.precio}")

print(f"el nombre el libro se llama {mi_libro1.nombre_libro} y su autor es {mi_libro1.autor} precio: {mi_libro1.precio}, el codigo del libro: {mi_libro1.codigo}")

#Libro 2

mi_libro2 = Libro ("FCA983", "Pie de guerra", "Carlos Cuauhtemoc Sanchez", 120000)


print(mi_libro2.precio)
print(mi_libro2.autor)
print(mi_libro2.nombre_libro)
print(mi_libro2.codigo)

print(f"El precio del libro 2 es: {mi_libro2.precio}")
print(f"El autor del libro 2 es: {mi_libro2.autor}")
print(f"el nombre del libro 2 es: {mi_libro2.nombre_libro}")
print(f"El codigo del libro 2 es: {mi_libro2.codigo}")
print(f"el nombre el libro se llama {mi_libro2.nombre_libro} y su autor es {mi_libro2.autor} precio: {mi_libro2.precio}, el codigo del libro: {mi_libro2.codigo}")

#Libro 3

mi_libro3 = Libro ("HTS678", "Diario de ana frank", "Ana Frank", 70000)

print(mi_libro3.precio)
print(mi_libro3.autor)
print(mi_libro3.nombre_libro)
print(mi_libro3.codigo)

print(f"El precio del libro 3 es: {mi_libro3.precio}")
print(f"El autor del libro 3 es: {mi_libro3.autor}")
print(f"el nombre del libro 3 es: {mi_libro3.nombre_libro}")
print(f"El codigo del libro 3 es: {mi_libro3.codigo}")
print(f"el nombre el libro se llama {mi_libro3.nombre_libro} y su autor es {mi_libro3.autor} precio: {mi_libro3.precio}, el codigo del libro: {mi_libro3.codigo}")

#Libro 4

mi_libro4 = Libro ("KMJ412", "Memento mori", "César Pérez Gellida", 36000)

print(mi_libro4.precio)
print(mi_libro4.autor)
print(mi_libro4.nombre_libro)
print(mi_libro4.codigo)

print(f"El precio del libro 4 es: {mi_libro4.precio}")
print(f"El autor del libro 4 es: {mi_libro4.autor}")
print(f"el nombre del libro 4 es: {mi_libro4.nombre_libro}")
print(f"El codigo del libro 4 es: {mi_libro4.codigo}")
print(f"el nombre el libro se llama {mi_libro4.nombre_libro} y su autor es {mi_libro4.autor} precio: {mi_libro4.precio}, el codigo del libro: {mi_libro4.codigo}")
