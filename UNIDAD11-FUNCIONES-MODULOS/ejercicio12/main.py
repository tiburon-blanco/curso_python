# Escriba un programa donde se le pida a varios usuarios (WHILE) el nombre y la edad.
# Si la persona es menor de edad (<18) se debe guardar el nombre en una lista llamada "menores"
# Si la persona es mayor de edad (>=18) se debe guardar el nombre en otra lista llamada "mayores"
# Se deber crear 2 funciones donde cada una maneje su lista.
# Al finalizar, imprimir cuantas personas hay en cada lista (menores y mayores)
# Consejo: crear un módulo (otro archivo) que maneje las funciones y sus listas True
# Necesito saber para invertir si hay mas mayores  o menores.

from func12 import *

seguir = True

while seguir:
    nombre=input("ingrese su nombre: ")
    edad= int(input("ingrese su edad:"))
    if edad<= 18:
         agregar_menores(nombre)
    else:
        agregar_mayor(nombre)
    cola=input("Hay mas personas para registrar: S/N: ")
    if cola == "N": 
        seguir = False

print("la lista de menores es: ", len(ver_lista_menores()))

print("la lista de mayores es: ", len(ver_lista_mayores()))

informe=ver_informe()

if informe != "iguales":
    print("el informe final es hay mas: ", informe)
else:
    print("el informe final da como resultado que son iguales la cantidad de mayore y menores")



