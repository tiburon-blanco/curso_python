# Escriba un programa donde se le pida a varios usuarios (WHILE) el nombre y la edad.
# Si la persona es menor de edad (<18) se debe guardar el nombre en una lista llamada "menores"
# Si la persona es mayor de edad (>=18) se debe guardar el nombre en otra lista llamada "mayores"
# Se deber crear 2 funciones donde cada una maneje su lista.
# Al finalizar, imprimir cuantas personas hay en cada lista (menores y mayores)
# Consejo: crear un módulo (otro archivo) que maneje las funciones y sus listas True

from func12 import *

seguir = True

ver_mayores=mayores
ver_menores=menores

# menores={}

while seguir:
    nombre=input("ingrese su nombre: ")
    edad= int(input("ingrese su edad:"))
    mayores(nombre, edad)
    menores(nombre, edad)
    cola=input("Hay mas personas para registrar: S/N: ")
    if cola == "N": 
        seguir = False

print("la lista de menores es: ", ver_menores)

print("la lista de mayores es: ", ver_mayores)





# while seguir:
#     nombre=input("ingrese su nombre: ")
#     edad= int(input("ingrese su edad:"))
#     if edad >= 18:
#         mayores[nombre]= edad
#     else:
#         menores[nombre]= edad
#     cola=input("Hay mas personas para registrar: S/N: ")
#     if cola == "N": 
#         seguir = False

# print("la lista de menores es: ", menores)

# print("la lista de mayores es: ", mayores)