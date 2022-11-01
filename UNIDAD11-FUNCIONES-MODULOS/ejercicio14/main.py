# Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 u 8 dígitos.



def dnivalido():

    dni = input("ingrese su dni: ")

    if len(dni) >= 7 and len(dni) <= 8:
        print("El dni ingresado es verdadero")
    else:
        print("El dni ingresado es invalido")

    return dni

# dni=dnivalido()

dnivalido()
