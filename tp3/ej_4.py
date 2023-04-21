class FacturaBuilder:
    def __init__(self, importe):
        self.importe = importe
        self.condicion_impositiva = ""

    def con_iva_responsable(self):
        self.condicion_impositiva = "IVA Responsable"
        return self

    def con_iva_no_inscripto(self):
        self.condicion_impositiva = "IVA No Inscripto"
        return self

    def con_iva_exento(self):
        self.condicion_impositiva = "IVA Exento"
        return self

    def construir(self):
        return Factura(self.importe, self.condicion_impositiva)


class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva

    def imprimir_factura(self):
        print("Factura:")
        print("Importe: $", self.importe)
        print("Condición impositiva: ", self.condicion_impositiva)


while True:
    # Pedimos al usuario que ingrese el importe de la factura
    importe = float(input("Ingrese el importe de la factura (o 'salir' para salir): "))

    if importe == "salir":
        break

    # Creamos las diferentes facturas en base a la condición impositiva del cliente
    factura_responsable = FacturaBuilder(importe).con_iva_responsable().construir()
    factura_no_inscripto = FacturaBuilder(importe).con_iva_no_inscripto().construir()
    factura_exento = FacturaBuilder(importe).con_iva_exento().construir()

    # Imprimimos las facturas
    factura_responsable.imprimir_factura()
    factura_no_inscripto.imprimir_factura()
    factura_exento.imprimir_factura()
