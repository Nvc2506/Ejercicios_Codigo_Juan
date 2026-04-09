def agregar_muebles(lista_nombres, elementos):
    if isinstance(elementos, str) and 1 <= len(elementos) <= 50:
        lista_nombres.append(elementos.title())
        print(f"elemento agregado {elementos.title()}")
    else:
        print("elementos invalido debe ser de 1 a 50 elementos")

def mostrar_muebles(lista_nombres):
    for mueble in lista_nombres:
        print(f"-> {mueble}") 

def modificar_nombre(lista_nombre, indice, nuevo_nombre):
    if not isinstance(nuevo_nombre, str) and 1 <= len(nuevo_nombre) <= 50:
        print("nombre de elemento invalido debe tener entre 1 a 50 caracteres")
        return
    if 0 <= indice < len(lista_nombre):
        nombre_original = lista_nombre[indice]
        lista_nombre[indice] = nuevo_nombre.title()
        print(f"el elemnto {nombre_original} fue remplazado por {nuevo_nombre.title()}")
    else:
        print("no se encontro el nuevo elemento")

def borrar_elemento(lista_nombre, indice):
    if 0 <= indice <len(lista_nombre):
        borrar = lista_nombre.pop(indice)
        print(f"el cliente {borrar}, se borro de la lista el elemento")
    else:
        print("no se borro el elemento")

def main():
    muebles = ["escritorio","silla","casilleros"]
    print("muebles actuales")
    mostrar_muebles(muebles)

    agregar_muebles(muebles, "tablero")
    mostrar_muebles(muebles)

if __name__ == "__main__":
    main()