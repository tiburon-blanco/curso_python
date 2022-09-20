# Crear un diccionario con los números primos hasta el 10
# Donde la KEY es el nombre del número
# El VALUE es el número
# Luego agregar el 31 al diccionario
# Luego eliminar los 2 primeros
# Mostrar el diccionario en pantalla

n_primos={"dos": 2,"tres": 3,"Cinco": 5, "Siete": 7,}

print(n_primos)

n_primos["Treinta y uno"]=31

print(n_primos)

n_primos.pop("dos")
n_primos.pop("tres")

print(n_primos)
