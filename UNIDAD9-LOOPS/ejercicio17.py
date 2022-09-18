# MATRICES
# Dada la siguiente matriz
# matriz = [
#            [1,2,4,7,2],
#            [7,9,1,7,8],
#            [4,5,1,3,3],
#            [6,3,7,9,2],
#          ]
# Contar la cantidad de un número especifico ingresado por teclado

matriz=[ [1,2,4,7,2],
          [7,9,1,7,8],
          [4,5,1,3,3],
          [6,3,7,9,2],
          ]

n=int(input("Ingrese un numeor a buscar en la matriz: "))

seguir=True
contador=0

while seguir:
    if n in matriz:
        contador=+1
    print(contador)
else:
        seguir=False


