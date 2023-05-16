## armar una matriz bidimensonial de 10*10 y que aleatoriamente mediante un algoritmo introduzca 0 y 1 y despues poder consultar cuantos 0 y 1 hay?##

# 1- crear una matriz
# 2- algoritmo de llenado
# 3- consulta


print("1-________ CREAR UNA MATRIZ_________________")

matriz = []

filas = int(input("ingrese la cantidad de filas de la matriz: "))
columnas = int(input("ingrese la cantidad de columnas de la matriz: "))


for f in range(filas):
    for c in range(columnas):
        print(0, end=' ')
    print('')
