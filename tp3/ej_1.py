class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class FactorialCalculator(metaclass=SingletonMeta):

    def __init__(self, n):
        self._n = n

    def calculate(self):
        if not hasattr(self, '_result'):
            self._result = 1
            for i in range(1, self._n+1):
                self._result *= i
        return self._result


if __name__ == '__main__':
    n = int(input("Ingrese el número para calcular su factorial: "))

    calculator = FactorialCalculator(n)
    print(f"{n}! = {calculator.calculate()}")
