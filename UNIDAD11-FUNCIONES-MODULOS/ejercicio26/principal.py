
import os

def clean():
  os.system('clear')

def menu():
    print("********* AGENDA **********")
    print("* 1 - Ver Listado         *")
    print("* 2 - Agregar             *")
    print("* 3 - Buscar              *")
    print("* 4 - Eliminar            *")
    print("* 5 - Salir               *")
    print("***************************")
    print("* Seleccione una opción ***")
    print("***************************")


def selectOption():
    option = input()
    if not option.isdigit():
      clean()
      print("Error: debe ingrear un valor numero entre 1 y 5")
      print("[Enter] para continuar")
      input()
    return option

def longitud_pila(pila):
    return len(pila)



#  Función que devuelve si la pila está vacía, no tiene elementos.
def estavaciapila (pila):
    if pila == 0:
      return print("La pila esta vacia")

## return len(pila)=0


# Función que devuelve si la pila está llena.  
def estallenapila():

    return
# Función que recibe una cadena de caracteres y añade la cadena a la pila,
#  si no está llena. si esta llena muestra un mensaje de error.
def AgregarAPila(elementos, pila):
    return pila.append(elementos)
   


# Función que devuelve el último elemento añadido y lo borra de la pila. 
# Si la pila está vacía muestra un mensaje de error.     
# def SacarDeLaPila(pila):    x= pila.pop[(-1)]
#     return


# Función que muestra en pantalla los elementos de la pila. 
def VerPila(pila): 
    return pila