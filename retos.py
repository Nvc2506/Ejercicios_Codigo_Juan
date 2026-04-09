class Proveedores:
    def __init__(self, uniformes, pantallas, teclados, materiales, proyectores):
        self.uniformes = uniformes
        self.pantallas = pantallas
        self.teclados = teclados
        self.materiales = materiales
        self.proyectores = proyectores

    def get_uniformes(self):
        return self.uniformes

    def get_pantallas(self):
        return self.pantallas

    def get_teclados(self):
        return self.teclados

    def get_materiales(self):
        return self.materiales

    def get_proyectores(self):
        return self.proyectores

#--------------------------------------------------------------

    def set_uniformes(self, nueva_cantidad_uniformes):
        self.uniformes = nueva_cantidad_uniformes

        if isinstance(nueva_cantidad_uniformes, (int, float)) and nueva_cantidad_uniformes >0:
            self.uniformes = nueva_cantidad_uniformes
        else:
            raise ValueError("la cantidad de uniformes debe ser un numero")
        
    def set_proyectores(self, nueva_cantidad_proyectores):
        self.proyectores = nueva_cantidad_proyectores

        if isinstance(nueva_cantidad_proyectores, (int, float)) and nueva_cantidad_proyectores >0:
            self.proyectores = nueva_cantidad_proyectores
        else:
            raise ValueError("la cantidad de proyectores debe ser un numero")
        
    def set_materiales(self, nueva_cantidad_materiales):
        self.materiales = nueva_cantidad_materiales

        if isinstance(nueva_cantidad_materiales, (int, float)) and nueva_cantidad_materiales >0:
            self.materiales = nueva_cantidad_materiales
        else:
            raise ValueError("la cantidad de materiales debe ser un numero")
        


        
def main():
    print("PROVEEDORES")
    proveedores1 = Proveedores("Unidad de Uniformes",100.000)
    proveedores2 = Proveedores("Unidad de Pantallas",500.000)
    proveedores3 = Proveedores("Unidad de Teclados", 600.000)
    proveedores4 = Proveedores("Unidad de materiales", 800.000)
    proveedores5 = Proveedores("Unidad de proyectores", 200.000)

    print("Informacion de proveedores")
    proveedores1.mostrar_info()
    proveedores2.mostrar_info()
    proveedores3.mostrar_info()
    proveedores4.mostrar_info()
    proveedores5.mostrar_info()

if __name__ == "__main__":
    main()