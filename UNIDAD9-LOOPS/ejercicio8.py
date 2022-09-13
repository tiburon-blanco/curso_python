# WHILE
# Data la siguiente lista:
# n = [4,6,8,1,6,15,5,20]
# Recorrer con WHILE hasta que encuentre un número mayor a 10

#Declaraciones del búcle While // Python utiliza el bucle while de forma similar a otros lenguajes populares. 
# #El bucle while evalúa una condición y luego ejecuta un bloque de código si la condición es verdadera. #
# El bloque de código se ejecuta repetidamente hasta que la condición llega ser o es falsa.
#La sintaxis básica es:
# contador = 0
# while contador < 10:
   # Ejecuta el bloque de código aquí
   # Siempre que el contador sea inferior a 10




n = [4,6,8,1,6,15,5,20]
seguir = True
index = 0
while seguir:

    value = n[index]
    print(value)
    if value > 7:
        seguir = False
    index = index + 1
    


        