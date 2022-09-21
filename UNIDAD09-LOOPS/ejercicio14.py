# Escribir un programa que pregunte cuántos números se van a introducir.
# Luego pida esos números, 
# Después calcule su promedio.

numeros=int(input("Cuantos numeros va a introducir: "))

contador=0 
promedio=0

seguir=True

while seguir:
    if numeros==contador:
        seguir=False
    else:
        n=int(input("ingrese esos numeros: "))
        promedio=promedio+n
    contador= contador+1


print("El promedio de los numeros ingresados es: ", promedio/numeros)