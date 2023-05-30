def crear_tablero(x):
    tablero = []
    for i in range(x):
        fila = [0] * x
        tablero.append(fila)
    return tablero
