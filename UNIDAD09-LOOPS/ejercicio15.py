# Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
# Al finalizar, mostrar la suma de los números negativos y el promedio de los positivos.
# Hacer con FOR

print("ingrese 6 numeros enteros: ")

lista=[]
contador=0 

seguir=True

while seguir:
    if contador==6:
        seguir=False
    else:
        n=int(input("ingrese un numero: "))
        lista.append(n)
    contador= contador+1

print(lista)

negativos=[]
positivos=[]

for i in lista: 
    if i< 0: 
       negativos.append(i)
    else:
        positivos.append(i)    

print("la suma de los numeros negativos arroja como resultado: ", sum(negativos))

print("el promedio de los numeros positivos es: ", sum(positivos)/ len(positivos))




