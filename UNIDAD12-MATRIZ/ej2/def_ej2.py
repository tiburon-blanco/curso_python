import random


def c_matriz(x, y):
    matriz = []
    for f in range(x):
        fila = []
        for c in range(y):
            numero = 0
            fila.append(numero)
            print(numero, end=' ')
        print(' ')
        matriz.append(fila)
    return matriz


# de aca obtengo las posiciones a reemplazar por 1
def coordenadas_remplazo(c, x, y):
    coordenadas = []
    for i in range(c):
        fila_aleatoria = random.randint(0, x-1)
        columna_aleatoria = random.randint(0, y-1)
        coordenadas.append([fila_aleatoria, columna_aleatoria])
    return coordenadas


def cantidad_a_colocar(x, y):
    resultado = round((x*y)*0.1)
    return resultado
