
def mostrar_inventario(productos):
    print("mostrar inventario actual")
    if not productos:
        print("no hay productos registrados")
        return
    for i, producto in enumerate(productos, start=1) :
        print(f"{i}. {producto['nombre']} -{producto['precio']}:.2f")

def mostrar_inventario(productos):
    print("inventario actual")
    if not productos: 
        print("no hay productos registrados")
        return
    for i, productos in enumerate(productos, start=1):
        print(f"Inv-{i}. {productos['nombre']} - ${productos['precio']:.2f}")



def main ():
    # crearemos nuestro inventario inicial lo que existe en el momento
    inventario = [
        {"nombre", "taladro","precio", 150000},
        {"nombre", "martillo","precio",400000},
        {"nombre", "destornillador","precio",150000}

    ]

if __name__ == "__main__":
    main()