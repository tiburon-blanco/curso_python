import random
import collections

## armar una matriz bidimensonial de 10*10 y que aleatoriamente mediante un algoritmo introduzca 0 y 1 y despues poder consultar cuantos 0 y 1 hay?##

# 1- crear una matriz
# 2- algoritmo de llenado
# 3- consulta


print("1-________ CREAR UNA MATRIZ_________________")


filas = int(input("ingrese la cantidad de filas de la matriz: "))
columnas = int(input("ingrese la cantidad de columnas de la matriz: "))


def crear_matriz(fil, col):
    matriz = []
    for f in range(fil):
        fila = []
        for c in range(col):
            numero = random.randint(1, 2)
            fila.append(numero)
            print(numero, end=' ')
        print('')
        matriz.append(fila)
    return matriz


matriz = crear_matriz(filas, columnas)
print(matriz)
