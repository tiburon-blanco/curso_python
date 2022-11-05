# Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 u 8 dígitos.



def dnivalido(dni):

    if len(dni) >= 7 and len(dni) <= 8:
            return True
    else:
            return False

    

# dni=dnivalido()

dni = input("ingrese su dni: ")

esvalido=dnivalido(dni)
