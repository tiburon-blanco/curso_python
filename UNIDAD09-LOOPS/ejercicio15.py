# Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
# Al finalizar, mostrar la suma de los números negativos y el promedio de los positivos.
# Hacer con FOR

print("ingrese 6 numeros enteros: ")

positivo=0
negativos=0
contador=0 

seguir=True

while seguir:
    if contador==6:
        seguir=False
    else:
        n=int(input("ingrese un numero: "))
        if n>0:
            positivo=positivo+n
        elif n<0:
            negativos=negativos+n
    contador= contador+1

print(positivo)

print(negativos)

print("la suma de los numeros positivos arroja como resultado: ", positivo)

print("el promedio de los numeros negativos es: ", negativos)




