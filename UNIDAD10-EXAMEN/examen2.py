# EXAMEN 2
# El intendente Juan Perez tiene como tarea poner 3 semáforos en su ciudad llamada "La Ideal".
# "La ideal" es un pueblo de 5 x 5 manzanas donde ocurren muchos accidentes.
# "La ideal" es una ciudad parecida a "La Plata" donde sus calles se llaman por números
# La numeración de las 5 cuadras horizontales van del 1 al 5
# La numeración de las 5 cuadras verticales van del 6 al 10

# El problema que tiene el intendente es: en qué calle debe poner los 3 semáforos?
# Al intendente se le ocurre la siguiente idea:
# Va a registrar los accidentes que ocurren en cada esquina durante el último mes y
# en las esquinas más accidentadas va a poner los 3 semáforos.

# Por ejemplo, una esquina puede ser: 4 y 7

# Cree un sistema donde se registren accidentes para que al final del mes 
# el intendente pueda saber en que esquinas deba cocolar los 3 semáforos.

matriz = [
        [0,0,0,4,0],
        [0,3,0,0,0],
        [0,0,5,0,0],
        [0,8,0,9,0],
        [0,0,0,0,20],
          ]

print(matriz)

print("registro de accidentes")

registro_accidentes=[]

calle_horizontales=[1,2,3,4,5]
calle_verticales=[6,7,8,9,10]

hay_accidentes=True

while hay_accidentes:
    direcciones_validas=True
    while direcciones_validas:
        direcciones_accidentes_hotizontal=int(input("ingrese calle horizontal donde ocurrio el accidente: "))
        if direcciones_accidentes_hotizontal not in calle_horizontales:
            print("direccion horizonatal invalida, debe estar entre las calles 1 y 5, ingres nuevamente: ")
            break
            
        direcciones_accidentes_vertical=int(input("ingrese calle vertical donde ocurrio  el accidente: "))
        if  direcciones_accidentes_vertical  not in calle_verticales:
            print("direccion vertical invalida, debe estar entre las calles 6 y 10, ingres nuevamente: ")
            break
        
        d_h=direcciones_accidentes_hotizontal - 1
        d_v=direcciones_accidentes_vertical-6
      
      
        matriz[d_h][d_v]= matriz[d_h][d_v] + 1
        direcciones_validas=False
    nuevo_registro=input("Existe otro accidente: S/N ")
    if nuevo_registro.upper() == "N":
        hay_accidentes=False

maximo=0
calle_i=0
calle_j=0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]>maximo:
            maximo=matriz[i][j]
            calle_i=i
            calle_j=j


maximo_1=0
calle_i_1=0
calle_j_1=0


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if (calle_i !=i and calle_j !=j):
            if matriz[i][j]>maximo_1 :
                maximo_1=matriz[i][j]
                calle_i_1=i
                calle_j_1=j

maximo_2=0
calle_i_2=0
calle_j_2=0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if ((calle_i !=i and calle_j !=j) and (calle_i_1 !=i and calle_j_1 !=j)):
            if matriz[i][j]>maximo_2:
                maximo_2=matriz[i][j]
                calle_i_2=i
                calle_j_2=j


print("El intendende Juan Perez, decidio colocar el primer semaforo en la calle: ", calle_i + 1, "y", calle_j + 6, "porque ocurrieron ", maximo, "accidentes.")

print("El intendende Juan Perez, decidio colocar el 2  semaforo en la calle: ", calle_i_1 + 1, "y", calle_j_1 + 6, "porque ocurrieron ", maximo_1, "accidentes.")

print("El intendende Juan Perez, decidio colocar el tercer semaforo en la calle: ", calle_i_2 + 1, "y", calle_j_2 + 6, "porque ocurrieron ", maximo_2, "accidentes.")



