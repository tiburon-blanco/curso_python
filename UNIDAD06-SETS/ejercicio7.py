# OPERADORES de sets o conjuntos &  |  -
# & = Intersessión
# | = Conjunción
# - = Diferencia
# Dados los sets: 
# a = {3, 4, 5, 6}
# b = {4, 5, 8, 9}
# Mueste en pantalla Intersessión y la Conjunción
# Mueste la diferencia entre los sets. Es lo mismo hacer (a-b) que (b-a)

a = {3, 4, 5, 6}
b = {4, 5, 8, 9}


c=a&b
print("El resultado de la interseccion de los set a y b es: ", c)

c=a|b
print("El resultado de la conjuncion de los set a y b es: ", c)

c=(a-b)
print("El resultado de la diferencia de los set a - b es: ", c)

c=(b-a)
print("El resultado de la interseccion de los set  b-a es: ", c)