# EXTEND
# Dada la siguiente lista:
# lista = [3, "HOLA", True, [2, 3, 6], "Mundo", 8]
# Extender la lista con el elemento 10
# Extender la lista con la lista [7, 2] (Notar la diferencia con el ejercio anterior, osea APPEND)
# Cual es la diferecnia entre APPEND y EXTEND?

lista=[3, "HOLA", True, [2, 3, 6], "Mundo", 8]

print(lista)

lista.extend([10])
print(lista)

lista.extend([[7,2]])
print(lista)

print(len(lista))

# la diferencia entre append y extend es que  append() agrega un elemento al final de la lista 
# mientras que . extend() puede agregar varios elementos de una secuencia al final de la lista.

