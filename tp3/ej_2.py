class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class TaxCalculator(metaclass=SingletonMeta):

    def __init__(self):
        self._iva_rate = 0.21
        self._iibb_rate = 0.05
        self._municipal_rate = 0.012

    def calculate_taxes(self, base_imponible):
        iva = base_imponible * self._iva_rate
        iibb = base_imponible * self._iibb_rate
        municipal = base_imponible * self._municipal_rate
        total_taxes = iva + iibb + municipal
        return total_taxes


if __name__ == '__main__':
    tax_calculator = TaxCalculator()
    base_imponible = float(input("Ingrese el valor de la base imponible: "))
    taxes = tax_calculator.calculate_taxes(base_imponible)
    print(f"Impuestos para una base imponible de {base_imponible}: {taxes}")
