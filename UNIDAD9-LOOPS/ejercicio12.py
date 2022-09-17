# Encuentra la suma de todos los números pares del 1 al 100


numeros_pares=[]

for i in range(0,100,2):
        numeros_pares.append(i)
        
print(numeros_pares)

print("La suma de todos los numero pares del 1 al 100 es: ", sum(numeros_pares))
