import random


def crear_tablero(x):
    tablero = []
    for i in range(x):
        fila = [0] * x
        tablero.append(fila)
    return tablero


def coordenadas_remplazo(x):
    coordenadas = []
    for i in range(x):
        fila_aleatoria = random.randint(0, x-1)
        columna_aleatoria = random.randint(0, x-1)
        coordenadas.append([fila_aleatoria, columna_aleatoria])
    return coordenadas
