# MATRICES 
# Dada la siguiente matriz de 5 x 3

# matriz = [
#            [1,2,4,7,2],
#            [7,9,1,7,8],
#            [4,5,1,3,3]
#          ]


# 1) Mostrar el valor de la poscion [1][1]
# 2) Mostrar la cantidad de elemtos que tiene
# 3) Contar la cantidad de 3 que tiene la fila 2 (Recordar que la primer fila es la 0)
# 4) Cual es el indice del número 9 de la fila 1
# 5) Ordernar la primer fila (Fila 0) y mostrar en pantalla la primer fila
# 6) Extender la matriz con la siguiente lista [6,3,7,9,2] y mostrar la matriz

matriz = [
         [1,2,4,7,2],
         [7,9,1,7,8],
         [4,5,1,3,3]
          ]

print("1) El valor de la posicion 1,1 es: ", matriz[1][1])

print("2) La cantidad de elementos de la matriz es: ", len(matriz))


n=matriz[2]



print("3) La cantidad de 3 que tiene la fila 2 es: ", n.count(3))


n_4=matriz[1]

print("4) El indice del numero 9 de la fila 1 es:  ",n_4.index(9) )

n_5=matriz[0]
x=n_5.sort()

print("5) El orden de la fila 0 es:  ",n_5 )

print( "6) Extender la matriz con la siguiente lista [6,3,7,9,2] y mostrar la matriz")

matriz.append([6,3,7,9,2])

print(matriz)