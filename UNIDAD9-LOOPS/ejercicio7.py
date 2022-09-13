# Data la siguiente lista:
# lista = [5, 14, 7, 23, 31, 5, 32, 19]

# Ingresar por teclado un número y buscar la posición dentro de la lista
# A) Hacer el ejercio con FOR, ENUMERATE, IF
# B) Hacer el ejercio sin FOR (Ver unidades anteriores usando INDEX)

# Que opción en mejor A o B y porque?



lista = [5, 14, 7, 23, 31, 5, 32, 19]

valor=int(input("ingrese por teclado un numero entero: "))

for index, x in enumerate(lista):
    if (x==valor):
        print (index)



## B)


