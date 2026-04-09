# inventario de una ferreteria
# metodo append() agregar datos
# simular un sistema de control de inventario
# 1 agregar nuevos productos append()
# 2 insertar productos en una posicion especificca insert()
# 3 eliminar productos agotados remove() o pop()
# ordenar productos por nombre y precio sort()
# validar las entradas de los datos 

def mostrar_inventario(productos):
    print("inventario actual")
    if not productos: 
        print("no hay productos registrados")
        return
    for i, productos in enumerate(productos, start=1):
        print(f"Inv-{i}. {productos['nombre']} - ${productos['precio']:.2f}")

def agregar_productos(productos, nombre, precio):
    # validar entrada de datos
    if isinstance(nombre, str) and nombre.strip() and nombre != isinstance(precio,(int, float)) and precio > 0:
        productos.append({"nombre": nombre.title().strip(), "precio": precio})
    else:
        print("Datos invalidos, nombre deber ser un texto y el precio un valor positivo")


def insertar_productos(productos, indice, nombre, precio):
    if 0 <- indice <-len(productos) and isinstance(precio(int, float)) and precio > 0:
        productos.insert(indice, {"nombrer": nombre.title().strip(), "precio": precio})
        print(f"el producto{nombre.title()} fue agregado exitosamente")

# 3 eliminar productos agotados remove() o pop()

def eliminar_producto(producto, nombre):
    for productos in productos: 
        if nombre["nombre"].lower() == nombre.lower():
            producto.remove(nombre)
        print(f"Producto {nombre.title()} eliminado del inventario")
        return
    print("producto no encontrado")

def main ():
    # crearemos nuestro inventario inicial lo que existe en el momento
    inventario = [
        {"nombre": "taladro","precio": 150000},
        {"nombre": "martillo","precio":400000},
        {"nombre": "destornillador","precio":150000}

    ]
    mostrar_inventario(inventario)
    print("agregar elementos al iventario")
    nombre = input("nombre del elemento")
    precio = int(input("precio del elemento"))
    agregar_productos(inventario,nombre,precio)
    mostrar_inventario(inventario)
    insertar_productos(inventario, 2, "broca", 12000)
    mostrar_inventario(inventario)
    eliminar_producto(inventario,"martillo")
    mostrar_inventario(inventario)

if __name__ == "__main__":
    main()