# Escribir un programa que solicite al usuario 3 números e indique el menor de los tres.
# Los numero ingresados van a ser siempre distintos

x=int(input("ingrese el primer numero: "))
y=int(input("ingrese el segundo numero: "))
z=int(input("ingrese el tercer numero: "))

if x<y<z:
    print("El numero menor es: ", x)
if y<x<z:
    print("El numero menor es: ", y)
else:
    print("El numero menor es: ", z)

