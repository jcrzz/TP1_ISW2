from __future__ import annotations
from abc import ABC, abstractmethod


class TrenLaminador(ABC):
    """
    La clase abstracta TrenLaminador define la interfaz para los diferentes
    tipos de trenes laminadores. Cada clase concreta implementa el método
    producir para fabricar la lámina.
    """

    @abstractmethod
    def producir(self) -> str:
        pass


class TrenLaminador5(TrenLaminador):
    def producir(self) -> str:
        return "Produciendo lámina de 0.5” x 1.5 m en un tren laminador de 5 mts."


class TrenLaminador10(TrenLaminador):
    def producir(self) -> str:
        return "Produciendo lámina de 0.5” x 1.5 m en un tren laminador de 10 mts."


class Lamina:
    """
    La clase Lamina representa la lámina de acero que se enviará a producir a
    un tren laminador.
    """

    def __init__(self, espesor: float, ancho: float) -> None:
        self.espesor = espesor
        self.ancho = ancho

    def fabricar_lamina(self, tren_laminador: TrenLaminador) -> str:
        """
        El método fabricar_lamina acepta un objeto TrenLaminador y llama al
        método producir para fabricar la lámina en el tren laminador indicado.
        """
        return tren_laminador.producir()


if __name__ == "__main__":
    """
    El código de ejemplo muestra cómo crear una lámina y enviarla a un tren
    laminador para su producción.
    """

    # Creamos una lámina de acero de 0.5” x 1.5 m
    lamina = Lamina(0.5, 1.5)

    # Enviamos la lámina a un tren laminador de 5 mts.
    tren_laminador_5 = TrenLaminador5()
    resultado = lamina.fabricar_lamina(tren_laminador_5)
    print(resultado)

    # Enviamos la misma lámina a un tren laminador de 10 mts.
    tren_laminador_10 = TrenLaminador10()
    resultado = lamina.fabricar_lamina(tren_laminador_10)
    print(resultado)
