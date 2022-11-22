# Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
# todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
# La lista se debe carhar por teclado

from fun18 import *

lista_numeros=[]

continuar= True

while continuar:
    numeros=int(input("ingrese un numero: "))
    lista= lista_numeros.append(numeros)
    x= input("Desea ingresar mas numeros: s/n: ")   
    if x != "s":
        continuar= False

print("la suma de la lista es", lista_numeros) 

res_suma=suma(lista_numeros)

print("la suma de los numeros ingresados es: ", res_suma)

res_multi= mult(lista_numeros)

print("la suma de los numeros ingresados es: ", res_multi)






