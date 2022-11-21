# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
# devuelve False.

from func_17 import *

letra = input('Introduce una letra por favor: ')


vocal=es_vocal(letra)

if vocal == True:
    print ("la letra ingresada es una vocal.")
else:
    print("La letra ingresada NO es una vocal.")






# def validar_vocal(caracter):
#     if caracter == ("a" or "e" or "i" or "o" or "u"):
#         return True

# caracter=input("ingrese un caracter alfabetico: ")

# print("el caracter ingresado es: ", validar_vocal(caracter))  



