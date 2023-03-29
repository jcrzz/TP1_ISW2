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
    print("Debe ingresar un rango!")
    sys.exit()
else:
    rango = sys.argv[1]
    if "-" not in rango:
        print("Formato incorrecto del rango. Debe ser desde- o -hasta.")
        sys.exit()
    else:
        desde, hasta = rango.split("-")
        desde = 1 if desde == "" else int(desde)
        hasta = 60 if hasta == "" else int(hasta)

if desde > hasta:
    desde, hasta = hasta, desde

print("Calculando los factoriales entre", desde, "y", hasta, "...")

for num in range(desde, hasta+1):
    print("El factorial de", num, "es", factorial(num))
