# Ingrese el nombre de usuario y la contraseña;
# ¿Determine si el nombre de usuario y la contraseña son correctos? (name = "root", passwd = "citric")
# Como medida de seguridad, solo hay tres oportunidades para iniciar sesión. 
# Si hay más de tres oportunidades, se informará al usuario que la clave fue bloqueada


name= "root"
passwd= "citric"

seguir=True   
intentos=0

while seguir:
    usuario=input("ingrese su usuario: ")
    pasword=input("ingrese su passwd: ")

    if usuario==name:
        if pasword==passwd:
            print("Datos ingresados correctamente")
            seguir=False    
    else:
        intentos= intentos+1     
        print("ingrese nuevamente los datos: ") 
    if intentos==3:
                print("Clave Bloqueada")    
                seguir=False   
