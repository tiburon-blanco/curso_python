# EXAMEN PILA (LIFO)
# Vamos a crear un programa para trabajar con una pila. 
# Una pila es una estructura de datos que nos permite guardar un conjunto de variables. 
# La característica fundamental es que el último elemento que se añade 
# al conjunto es el primero que se puede sacar.

# Para representar una pila vamos a utilizar una lista de cadenas de caracteres.

# El tope de la pila es 10

# Vamos a crear varias funciones para trabajar con la pila:

# LongitudPila: Función que devuelve el número de elementos que tiene.
# EstaVaciaPila: Función que devuelve si la pila está vacía, no tiene elementos.
# EstaLlenaPila: Función que devuelve si la pila está llena.
# AgregarAPila: Función que recibe una cadena de caracteres y añade la cadena a la pila, si no está llena. si esta llena muestra un mensaje de error.
# SacarDeLaPila: Función que devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía muestra un mensaje de error.
# VerPila: Función que muestra en pantalla los elementos de la pila.

# Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones:

# Añadir elemento a la pila
# Sacar elemento de la pila
# Longitud de la pila
# Mostrar pila
# Salir

from db import pila 
pila = []

from principal import *

from ui import screen

continuar = True


while continuar:
    screen.clean()
    screen.menu()

    option = int(input())

    if option == 1:  # añadir
        print("1-Añadir elemento a la pila.")
        if longitud_pila(pila) >= 10:
            print("La pila ya esta completa")
            
        if longitud_pila(pila)< 10:
            elementos=input("agregar elemento:")
            AgregarAPila(elementos,pila)
            print("la pila ahora posee: ", longitud_pila(pila), "elementos." )
            print(pila)

    if option == 2: # sacar
        print("2-Sacar elemento de la pila")
        if longitud_pila(pila) > 1:
            pila.pop(-1)
            print(pila)
        else:
            print("Ya se encuentra vacia")
        

    if option == 3: # longitud
        print("La longitud de la pila es de", longitud_pila(pila), "elementos.")
        

    if option == 4:
        print("4-Mostrar pila", VerPila(pila))
        

    if option == 5:
        continuar = False