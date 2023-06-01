from def_ej3 import *
import random

# Crear una batalla naval de 1 solo jugador
# Tablero de 5x5
# Poner 2 barcos de 2x2 (Azar)
# Fin de juego: cuando elimine los 2 barcos o cuando llegue a 20 tiros o bombas tiradas.
# Indicar en cada tipo si fue agua, tocado o hundido
# Indicar si gano o perdio

print("1-____________________CREAR TABLERO____________")


x = int(input("ingrese el numero a hacer el tablero: "))

tablero = crear_tablero(x)

print("2-____________________IMPRIMIR TABLERO____________")

for fila in tablero:
    print(fila)

print("2-____________________PONER DOS BARCOS ALEATORIAMENTE____________")


def coordenadas_remplazo(x):
    coordenadas = []
    for i in range(x):
        fila_aleatoria = random.randint(0, x-1)
        columna_aleatoria = random.randint(0, x-1)
        coordenadas.append([fila_aleatoria, columna_aleatoria])
    return coordenadas


coordenadas = coordenadas_remplazo(2)
print(coordenadas)


print("3- Ingresar coordenadas de misiles")
