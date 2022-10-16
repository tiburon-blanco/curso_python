# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno mostrar la suma acumulada 
# Crear una función que realice dicha suma.
# La funcion debe recibir el valor y devolver la suma


from fun_c import *


seguir= True


while seguir:
    numero=int(input("ingrese numeros: "))
    if numero == 0:
         seguir = False
    else:
        sa= suma_acumulada(numero)
        print("la suma acumulada es: ", sa)
    



    



    
        
