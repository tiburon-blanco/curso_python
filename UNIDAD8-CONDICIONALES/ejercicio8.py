# En una empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser:

# Nivel	        Puntuación
# Inaceptable	0.0
# Aceptable	    0.4
# Meritorio	    0.6

# No valores intermedios entre las cifras mencionadas. 
# La cantidad de dinero conseguida en cada nivel es de $ 1.400 multiplicada por la puntuación del nivel.

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.

<<<<<<< HEAD


=======
>>>>>>> 65b626728ba341b44ff543058c030d2fc2b158e5
inaceptable = 0.0
aceptable	= 0.4
meritorio	= 0.6

beneficios=1500
nivel_seleccionado=0


puntaje=float(input("ingrese su puntaje: "))

if puntaje==inaceptable:
    nivel_seleccionado=inaceptable
if puntaje==aceptable:
    nivel_seleccionado=aceptable
if puntaje==meritorio:
    nivel_seleccionado=meritorio

calculo=nivel_seleccionado*beneficios

print("los beneficios obtenidos son: ", calculo)
