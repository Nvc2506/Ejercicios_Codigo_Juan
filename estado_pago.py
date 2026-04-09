from abc import ABC, abstractmethod
class GenerarReporte(ABC):
    @abstractmethod
    def ganerar_reporte(self) -> None:
        pass

class sistemapago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto
    @abstractmethod
    def procesar_pago(self) -> None:
        pass

class pagoBancario(sistemapago, GenerarReporte):
    def procesar_pago(self) -> None:
        print(f"procesando transferencia bamcaria por ${self.monto:,.2f}") 
    def ganerar_reporte(self) -> None:
        print("reporte de pago realizado mediante sistema bancario")

class pagoCripto(sistemapago):
    def procesar_pago(self) -> None:
        print(f"procesando pago cripto Moneda por ${self.monto:,.2f}")
    def ganerar_reporte(self) -> None:
        print("reporte de pago realizado mediante sistema bancario")

def ejecutar_pago(pago: sistemapago) -> None:
    pago.procesar_pago()

def main() -> None:
    print("+++++ SISTEMA DE PAGOS +++++")

    pago1 = pagoBancario(500000)
    pago2 = pagoCripto(750000)
    
    ejecutar_pago(pago1)
    pago1.ganerar_reporte()

    ejecutar_pago(pago2)
    pago2.ganerar_reporte()
    

if __name__ == "__main__":
    main()