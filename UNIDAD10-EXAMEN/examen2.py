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
           [1.6,1,1,1,1]
           [2,2,2,2,2]
           [3,3,3,3,3]
           [4,4,4,4,4]
           [5,5,5,5,5]
          ]

print(matriz)

contador=0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==True:
            contador=contador+1

print(contador)