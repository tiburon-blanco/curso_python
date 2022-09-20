# WHILE
# Escribír un programa donde se ingrese una contraseña.
# Luego le vuelve a pedir la contraña para confirmar si la escribió bien. 
# Repetir este proceso hasta que las contraseñas sean iguales.
# Caso contrario indicar que la ingreso mal para vovler a repetir el proceso.


contrasenia_igual = True

while contrasenia_igual:
        contrasenia_1=(input("ingrese su contraseña: "))
        contrasenia_2=(input("ingrese nuevamente su contraseña: "))
        if contrasenia_1==contrasenia_2:
           contrasenia_igual=False 

  
print("Contraseña Correcta")