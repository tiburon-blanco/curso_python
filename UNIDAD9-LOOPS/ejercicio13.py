# Escribir un programa que pregunte cuántos números se van a introducir.
# Luego pida esos números, 
# Después muestre el mayor


numeros=int(input("Cuantos numeros piensa ingresar: "))

lista=[]
contador=0 

seguir=True

while seguir:
    n=int(input("ingrese un numero: "))
    lista.append(n)
    
    contador=+1
    if numeros == contador:
        seguir=False 

            


