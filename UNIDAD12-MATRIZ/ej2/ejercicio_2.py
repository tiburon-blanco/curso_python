from def_ej2 import *
import random

# Crear un amtrix de X x Y con 0 (Ej 5x5)
# Inicializar con 5 valores con 1
# Comienza el juego, Se le pide al usuario que ingrese la pos X e Y y decir si en esa posicion se encuentra un 1.
# El juego termina cuando se encuentra un 1 o llego a 5 posibilidades de error.

print("-------------0- INGRESO DE FILAS Y COLUMNAS---------------")

x = int(input("ingrese la cantidad de filas: "))
y = int(input("ingrese la cantidad de columnas: "))


print("-------------1- CREAR MATRIZ DE 0---------------")

matriz = c_matriz(x, y)

print("-------------2- DETERMINAR CANTIDAD Y POSICIONES A REEMPLAZAR ALEATORIAMENTE---------------")

numero_sustituto = 1

cantidad = cantidad_a_colocar(x, y)

print("la cantidad de posiciones a reemplazar con numeros unos en la matriz es de: ", cantidad)


resultado_reemplazos = coordenadas_remplazo(cantidad, x, y)


contador = 0


print("-------------3- CONVERTIR NUEVA MATRIZ CON NUMEROS REEMPLAZADOS---------------")

for contador in range(cantidad):
    if contador < cantidad:
        convirtiendo_coordenadas = resultado_reemplazos[contador]
        pos_x, pos_y = convirtiendo_coordenadas
        matriz[pos_x][pos_y] = numero_sustituto
    else:
        break

print("-------------4- INGRESO DE PÓSICION X E Y VERIFICAR SI EN ESA POSICION ESTA EL 1----------------")


seguir = True
intentos = 0
aciertos = 0

while seguir:
    if intentos == 5:
        print("Ha superado la cantidad de intentos. Comienze de nuevo.")
        break
    if aciertos == cantidad:
        print("ha encontrado todos los unos en la matriz.")
        break
    ingrese_x = int(input("ingrese una coordenada fila: "))
    ingrese_y = int(input("ingrese una coordenada columna: "))
    if 0 <= ingrese_x < x-1 and 0 <= ingrese_y < y-1:
        if matriz[ingrese_x][ingrese_y] == 0:
            intentos += 1
            print("Fallo, en esta posicion hay un 0")
        elif matriz[ingrese_x][ingrese_y] == 1:
            aciertos += 1
            print("en esta posicion hay un numero 1")
    else:
        print("los numeros ingresados estan fuera de rango. Ingrese un numero hasta: ",
              x-1, "para las filas. Y: ", y-1, "para las columnas.")


print("Ha finalizado el juego ")

print("-------------5- MATRIZ DONDE SE UBICAN LOS NUMEROS 1 Y COORDENADAS DE LAS MISMAS----------------")


for fila in matriz:
    print(fila)

print(resultado_reemplazos)
