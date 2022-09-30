# Escribir un programa para calcular el IMC (Índice de masa corporal), luego imprimir
# IMC = peso / altura **2
# peso es el kilogramos
# altura en metros
# Crear un funion IMC en un modulo

from modulo import imc
from modulo2 import imc3

peso=float(input("ingrese peso: "))
altura=float(input("ingrese altura:"))
respusta = imc(peso, altura)
print("Su indice de masa corporal es: ",respusta)
