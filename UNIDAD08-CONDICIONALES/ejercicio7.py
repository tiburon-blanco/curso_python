# Escribir un programa que solicite al usuario una letra, si es una vocal, muestre el mensaje “es vocal”. 
# Se debe validar que el usuario ingrese un sólo carácter. 
# Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.

vocales=["a","e","i","o","u"]

x=(input("Ingrese una letra: "))

caracteres=len(x)

if caracteres>1:
    print("no se puede procesar el dato, debe ingresar solo un caracter:")

if caracteres==1:
    if x in vocales:
        print("es una vocal")
    else:
         print("no es una vocal")    