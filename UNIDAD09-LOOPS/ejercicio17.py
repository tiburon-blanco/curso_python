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
          [7,5,1,7,3],
          [6,3,7,9,2],
          ]

n=int(input("ingrese un numero por teclado: "))

contador=0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==n:
                contador=contador+1
        
print("La cantidad de elementos: ",n , " que hay en la matriz es de: ", contador)



print("Contando almacenando en listas::")
nn=[]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==n:
            nn.append(n)
        
print("la cantidad de elementos: ", n, "que hay en la matriz es",  len(nn))
  
        
        




