# Encuentra la suma de todos los números pares del 1 al 100

contador=0

for i in range(0,100,2):
        contador=contador+i
 
print("La suma de todos los numero pares del 1 al 100 utilizando una variable contador es: ", contador)


print("con listas")

print("con listas")
numeros_pares=[]

for i in range(0,100,2):
       numeros_pares.append(i)
        
print(numeros_pares)

print("La suma de todos los numero pares del 1 al 100 es: ", sum(numeros_pares))
