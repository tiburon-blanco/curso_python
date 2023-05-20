from def_ej1 import crear_matriz
import random
from collections import Counter

## armar una matriz bidimensonial de 10*10 y que aleatoriamente mediante un algoritmo introduzca 0 y 1 y despues poder consultar cuantos 0 y 1 hay?##

# 1- crear una matriz
# 2- algoritmo de llenado
# 3- consulta


print("1-________ CREAR UNA MATRIZ_________________")


filas = int(input("ingrese la cantidad de filas de la matriz: "))
columnas = int(input("ingrese la cantidad de columnas de la matriz: "))

matriz = crear_matriz(filas, columnas)


print("2- convierto la matriz en una lista para poder recorrerla")

print("cuento la cantidad de elementos que aparecen")


lista = []

for lista1 in matriz:
    for numero in lista1:
        lista.append(numero)


print("El numero 1 aparece: ", lista.count(1), "veces.")
print("El numero 2 aparece: ", lista.count(2), "veces.")
