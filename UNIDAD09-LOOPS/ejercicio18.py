# MATRICES
# Dada la siguiente matriz de booleanos
# matriz = [
#            [True,  False, True],
#            [True,  True,  False],
#            [False, True,  False],
#          ]
# Contar la cantidad de True

matriz = [
           [True,  False, True],
           [True,  True,  False],
           [False, True,  False],
          ]

contador=0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==True:
            contador=contador+1

print(contador)



print("Contando almacenando en listas::")

n=[]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==True:
            n.append(True)
        
print(n)
print(len(n))        

