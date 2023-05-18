import random


# cc = random.randrange(1, 10)

# print(cc)

# comienza = random.randint(0, 1)
# if comienza == 0:
#     print("comineza jugador ")
# else:
#     print("comienza pc")

# numero = random.randint(1, 166)

# print(numero)

matriz = []

filas = int(input("ingrese la cantidad de filas de la matriz: "))
columnas = int(input("ingrese la cantidad de columnas de la matriz: "))


def rellenar_matriz(filas, columnas):
    for f in range(filas):
        for c in range(columnas):
            print(random.randint(0, 1), end=' ')
        print('')
        return matriz


rellenar_matriz(filas, columnas)
