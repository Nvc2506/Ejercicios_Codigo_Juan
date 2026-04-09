# 1 Agregar nuevos clientes append()

def agregar_cliente(lista_cliente, nombre):
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_cliente.append(nombre.title())
        print(f"cliente agregado: {nombre.title()}")
    else:
        print("nombre de cliente invalido debe tener entre 2 a 50 caracteres")

# 2 Recorrer la lista y mostar los clientes for

def mostrar_cliente(lista_cliente):
    for cliente in lista_cliente:
        print(f"-> {cliente}")

# 3 Modificar un nombre en caso de errores

def modificar_cliente(lista_cliente, indice, nuevo_nombre):
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print("nombre de cliente invalido debe tener entre 2 a 50 caracteres")
        return # terminar la funcion
    if 0 <= indice < len(lista_cliente):
        nombre_original = lista_cliente[indice]
        lista_cliente[indice] = nuevo_nombre.title()
        print(f"El cliente {nombre_original} fue remplazado por {nuevo_nombre.title()}")
    else:
        print("No se encontro el dato, numero de la lista erronea")

# 4 Borrar un cliente 

def  borrar_cliente(lista_cliente, indice):
    if 0 <= indice < len(lista_cliente):
        borrar = lista_cliente.pop(indice)
        print(f"el cliente {borrar}, se borro de la lista cliente")
    else:
        print("no se encontro el cliente, cliente no borrado de la lista")

def main():
    clientes = ["hugo","paco","luis","mynniie"]
    print("clientes actuales")
    mostrar_cliente(clientes)

    # 1 Agregar nuevos clientes append()
    agregar_cliente(clientes, "alexander")
    mostrar_cliente(clientes)

    # 3 Modificar un nombre en caso de error 
    modificar_cliente(clientes,1,  "sapo")
    mostrar_cliente(clientes)

    # 4 Borrar un cliente
    borrar_cliente(clientes, 3)
    


if __name__ == "__main__":
    main()