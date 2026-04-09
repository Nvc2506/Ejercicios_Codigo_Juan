from dataclasses import dataclass

@dataclass
class Libro: #modelo de creacion de clases con el modelo internacional de calidad
    #respeta el pep 8, buenas practicas de la POO
    _titulo : str
    _autor: str
    _isbn : str
    _precio : float
#crear getter
@property
def titulo(self) -> str:
    #se obtiene el titulo del libro
    return self._titulo
#crear setter
@titulo.setter
def titulo(self,valor:str) -> None:
    #establece el titulo con validacion
    if isinstance(valor, str) and  valor.strip():
        self._titulo = valor
    else:
        raise ValueError ("El titulo debe ser un titulo valido")
    
@property   
def autor(self) -> str:
    return self._autor

@autor.setter
def autor(self,valor:str) -> None:
    if isinstance(valor, str) and valor.strip():
        self._autor = autor
    else:
        raise ValueError ("El autor debe ser un autor valido")

@property    
def isbn(self) -> str:
    return self._isbn

@isbn.setter
def isbn(self,valor:str) -> None:
    if isinstance(valor, str) and valor.strip():
        self._isbn = isbn
    else:
        raise ValueError ("El isbn debe serun isbn valido")
    
@property
def precio(self) -> float:
    return self._precio

@precio.getter
def precio(self,valor) -> None:
    if isinstance(valor, float) and valor.strip():
        self._precio = precio
    else:
        raise ValueError ("El precio debe ser un precio valido ")
    
# ---------------------------------------------------------------
#          Representacion segun estandar OOP & PEP 8
# ---------------------------------------------------------------

def __repr__(self) -> str:
    return(
        f"libro(titulo={self._titulo}, autor={self._autor},"
        f"isbn={self._isbn}, precio={self._precio})"
    )

# ---------------------------------------------------------------
#          Main (Demostracion)
# ---------------------------------------------------------------

def main() -> None:
    libro1 = Libro("python IA", "Pedrito Perez", "123-456-789", 120000.00)

    print("Informacion del Libro")
    print(libro1)

    libro1.precio = 150000.00
    libro1.titulo = "python Avanzado 3.0"

    print("Datos actualizados")
    print(libro1)
    libro1.isbn = "44444444"

    print("datos actualizados")
    print(libro1)

if __name__ == "__main__":
    main()
