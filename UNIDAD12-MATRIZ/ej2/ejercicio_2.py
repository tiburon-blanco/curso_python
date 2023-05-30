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

print("-------------2- DETERMINAR ALEATORIAMENTE POSICIONES A REEMPLAZAR---------------")

numero = 1
cantidad_a_colocar = round((x*y)*0.1)
print("se colocara el numero 1 en el 10 porciento de las posicionees de la matriz en total serian: ",
      cantidad_a_colocar, "veces.")


def coordenadas_remplazo(c):
    coordenadas = []
    for i in range(c):
        fila_aleatoria = random.randint(0, x-1)
        columna_aleatoria = random.randint(0, y-1)
        coordenadas.append([fila_aleatoria, columna_aleatoria])
    return coordenadas


resultado_reemplazos = coordenadas_remplazo(cantidad_a_colocar)
print(resultado_reemplazos)
# de aca obtengo las posiciones a reemplazar por 1


# convirtiendo_coordenadas= resultado_reemplazos[0]

# print(convirtiendo_coordenadas)


# desempaqueto la lista para que me de las dos posiciones de cada uno y poder acceder a x e y  y reemplazarlo por un 1

# pos_x, pos_y= convirtiendo_coordenadas

# x=pos_x
# y=pos_y

# print(x,y)

# matriz[x][y]= numero

# print(matriz)


# seguir=True
contador=0


# while seguir:
#     if contador <= cantidad_a_colocar:
#         convirtiendo_coordenadas=resultado_reemplazos[contador]
#         pos_x, pos_y= convirtiendo_coordenadas
#         matriz[pos_x][pos_y]=numero
#         contador=+1
#     if contador > cantidad_a_colocar:
#         seguir=False
# print(matriz)
  
        
 
print("-------------3- NUEVA MATRIZ CON NUMEROS REEMPLAZADOS---------------")

        
for contador in range(cantidad_a_colocar):
    if contador < cantidad_a_colocar:
        convirtiendo_coordenadas = resultado_reemplazos[contador]
        pos_x, pos_y = convirtiendo_coordenadas
        matriz[pos_x][pos_y] = numero
    else:
        break
        
 
for fila in matriz:
    print(fila)






# coordenada = resultado_reemplazos[]
# print("lalsals", coordenada)


print("-------------3- INGRESO DE PÓSICION X E Y VERIFICAR SI EN ESA POSICION ESTA EL 1----------------")




seguir=True
intentos=0

while seguir:
    if intentos== 2:
        seguir=False
    ingrese_X= int(input("ingrese una coordenada fila: "))
    ingrese_y= int(input("ingrese una coordenada columna: "))
    if matriz[ingrese_X] [ingrese_y] == 0:
        intentos+=1
        print("en esta posicion hay un 0")
    else:
        print("en esta posicion hay uno uno.")


print("Finalizo el juego---------------")
