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