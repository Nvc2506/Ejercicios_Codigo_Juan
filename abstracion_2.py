from abc import ABC, abstractmethod
class GenerarReportes(ABC): 
    @abstractmethod
    def generar_reportes(self) -> None:
        pass

class sistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto
    @abstractmethod
    def  procesar_pago(self) -> None:
        pass

class SistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto
    @abstractmethod
    def procesar_pago(self) -> None:
        pass

class PagoBancario(SistemaPago, GenerarReportes):
    def procesar_pago(self) -> None:
        print(f"procesando transferencia bancaria por {self.monto:,.2f}")

    def generar_reportes(self) -> None:
        print(f"reporte de pago bancario por {self.monto:,.2f}")

class PagoCriptomoneda(SistemaPago):
    def procesar_pago(self) -> None:
        print(f"procesando pago con criptomoneda por {self.monto:,.2f}")

def ejecutar_pago(pago: sistemaPago) -> None:
    pago.procesar_pago()

def main():
    pago1 = PagoBancario(500000)
    pago2 = PagoCriptomoneda(7600000)
    ejecutar_pago(pago1)
    pago1.generar_reportes()
    ejecutar_pago(pago2)

if __name__ == "__main__":
    main()