class Factorial:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
    
    def calculate_factorial(self, num):
        if num < 0:
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact
    
    def run(self):
        if self.min_num > self.max_num:
            self.min_num, self.max_num = self.max_num, self.min_num
        
        print("Calculando los factoriales entre", self.min_num, "y", self.max_num, "...")
        
        for num in range(self.min_num, self.max_num+1):
            result = self.calculate_factorial(num)
            if result is None:
                print("El factorial de un número negativo no existe")
            else:
                print("El factorial de", num, "! es", result)
factorial_obj = Factorial(1, 5) # Calcula los factoriales entre 1 y 5
factorial_obj.run()
