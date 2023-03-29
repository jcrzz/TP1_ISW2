#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
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

if len(sys.argv) < 2:                   #modificacion para que si no se ingresa el argumento, lo solicite
    num = int(input("Por favor, ingrese un número: "))
else:
    num = int(sys.argv[1])

print("El factorial de", num, "es", factorial(num))
