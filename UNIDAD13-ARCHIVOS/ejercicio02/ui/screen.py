import os
from db import agenda

def clean():
  os.system('clear')

def menu():
    print("* AGENDA ***********")
    print("* 1 - Ver agenda ***")
    print("* 2 - Buscar     ***")
    print("* 3 - Agregar    ***")
    print("* 4 - Editar     ***")
    print("* 5 - Eliminar   ***")
    print("* 6 - Salir      ***")
    print("********************")
    print("* Seleccionar ******")
    print("********************")


def menu_search():
    print("* BUSCAR ***********")
    print("* 1 - Por nombre ***")
    print("* 2 - Por numero  **")
    print("********************")
    print("* Seleccionar ******")
    print("********************")

def option1():
    data = agenda.obtenerAgenda()
    if len(data) == 0:
      print("* No hay datos en la agenda *")
    for key in data:
      print(key + " - " + data[key]);
    enter()


def option3():
  phone = input("Ingrese un numero de teléfono")
  name = input("Ingrese el nombre")
  agenda.agregar(phone, name)

def enter():
    print("* Enter para continuar *")
    input()  