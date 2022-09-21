# Escribir un programa que pregunte cuántos números se van a introducir.
# Luego pida esos números, 
# Después muestre el mayor


numeros=int(input("Cuantos numeros piensa ingresar: "))

maximo=0

contador=0 

seguir=True

while seguir:
    if numeros==contador:
        seguir=False
    else:
        n=int(input("ingrese un numero: "))
        if n>maximo:
            maximo=n
        contador= contador+1



print(maximo)

 

            


