# WHILE
# Escribír un programa donde se ingrese una contraseña.
# Luego le vuelve a pedir la contraña para confirmar si la escribió bien. 
# Repetir este proceso hasta que las contraseñas sean iguales.
# Caso contrario indicar que la ingreso mal para vovler a repetir el proceso.


contraseña=(input("ingrese su contraseña: "))

while contraseña != "salto evolutivo":
    contraseña=(input("Contraseña equivocada, ingrese nuevamente la constraseña: "))

print("Contraseña Correcta")