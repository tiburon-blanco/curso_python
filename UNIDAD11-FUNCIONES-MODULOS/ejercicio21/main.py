# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
# multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

from fun21 import *

caracter=input("ingrese un caracter: ")

veces= int(input("ingrese la cantidad que desea devolver: "))

res=generar_n_caracteres(caracter,veces)

print(res)


