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

n=int(input("Ingrese un numero a buscar en la matriz: "))

n_1=(len(matriz))
num_esp=[]

seguir=True
contador=0

while seguir:
    if contador==n_1:
        seguir=False
    
    if n in matriz [contador]:
        num_esp.append(n)
        contador=+1
    
print(len(num_esp))


        




