from abc import ABC, abstractmethod

class Comida(ABC):
    @abstractmethod
    def entregar(self):
        pass

class Hamburguesa(Comida):
    def entregar(self):
        return "Entrega de hamburguesa"

class ComidaFactory:
    def crear_comida(self, tipo_entrega):
        if tipo_entrega == "mostrador":
            return HamburguesaMostrador()
        elif tipo_entrega == "cliente":
            return HamburguesaCliente()
        elif tipo_entrega == "delivery":
            return HamburguesaDelivery()
        else:
            return None

class HamburguesaMostrador(Hamburguesa):
    def entregar(self):
        return "Hamburguesa en mostrador"

class HamburguesaCliente(Hamburguesa):
    def entregar(self):
        return "Hamburguesa retirada por el cliente"

class HamburguesaDelivery(Hamburguesa):
    def entregar(self):
        return "Hamburguesa entregada por delivery"


comida_factory = ComidaFactory()

while True:
    tipo_entrega = input("Especifique el tipo de entrega (mostrador, cliente, delivery): ")
    if tipo_entrega in ["mostrador", "cliente", "delivery"]:
        hamburguesa = comida_factory.crear_comida(tipo_entrega)
        print(hamburguesa.entregar())
    else:
        print("Tipo de entrega inválido. Intente de nuevo.")
    