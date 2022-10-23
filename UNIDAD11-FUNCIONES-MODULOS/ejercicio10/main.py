# Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un
# club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, 
# indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.
# Precondición: el formato del nombre de los socios será: nombre apellido. 
# Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. 
# Si un socio tuviera más de un apellido, el usuario sólo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. 
# En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, 
# la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. 
# 
# Ejemplo:
# Nombre: Martin Leonardo Antolini
# DNI: 30834970
# Martin8308

# Usar funciones para todo lo que se te acurra.
# Las funciones deben estar definidas en otro archivo

print("Ingreso de datos de usuario para darse de alta")



seguir= True

while seguir:
    registro_usuario()
    crear_identificador(dato)
    continuar=input("Desea ingresar un nuevo usuario: S/N")
    if continuar== "N":
        seguir:False