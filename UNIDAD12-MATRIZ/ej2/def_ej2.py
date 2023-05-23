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
