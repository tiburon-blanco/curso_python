from def_ej2 import *
import random

# Crear un amtrix de X x Y con 0 (Ej 5x5)
# Inicializar con 5 valores con 1
# Comienza el juego, Se le pide al usuario que ingrese la pos X e Y y decir si en esa posicion se encuentra un 1.
# El juego termina cuando se encuentra un 1 o llego a 5 posibilidades de error.

print("-------------0- INGRESO DE FILAS Y COLUMNAS---------------")

x = int(input("ingreses la cantidad de filas: "))
y = int(input("ingreses la cantidad de columnas: "))


print("-------------1- CREAR MATRIZ DE 0---------------")


matriz = c_matriz(x, y)

print("-------------2- COLOCAR ALEATORIAMENTE EN 5 POSICIONES UN NUMERO 1---------------")

numero = 1
cantidad_a_colocar = round((x*y)*0.1)
print("se colocara el numero 1 en el 10 porciento de las posicionees de la matriz en total serian: ",
      cantidad_a_colocar, "veces.")

coordenadas_aleatorias = random.sample(range(x*y), cantidad_a_colocar)

resultado = random.randint(0, x)
print(resultado)


print("-------------3- INGRESO DE PÓSICION X E Y VERIFICAR SI EN ESA POSICION ESTA EL 1----------------")
print("TIENE 5 INENTOS Y A POSTERIOR MUESTRA LA MATRIZ---------------")
