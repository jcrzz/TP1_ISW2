import sys

def factorial(num):
    if num < 0:
        print("El factorial de un número negativo no existe")
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

if len(sys.argv) < 2:
    input_str = input("Por favor, ingrese el rango de números en el formato desde-hasta: ")
    desde, hasta = map(int, input_str.split('-'))
else:
    desde, hasta = map(int, sys.argv[1].split('-'))

if desde > hasta:
    desde, hasta = hasta, desde

print("Calculando los factoriales entre", desde, "y", hasta, "...")

for num in range(desde, hasta+1):
    print("El factorial de", num, "es", factorial(num))
