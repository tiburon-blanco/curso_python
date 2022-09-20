# Escribir un programa que pregunte cuántos números se van a introducir.
# Luego pida esos números, 
# Después calcule su promedio.

numeros=int(input("Cuantos numeros va a introducir: "))

lista=[]
contador=0 

seguir=True

while seguir:
    if numeros==contador:
        seguir=False
    else:
        n=int(input("ingrese esos numeros: "))
        lista.append(n)
    contador= contador+1

promedio = sum(lista)/len(lista)
print("El promedio de los numeros ingresados es: ", promedio)