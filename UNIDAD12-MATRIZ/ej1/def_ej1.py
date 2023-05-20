import random


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
