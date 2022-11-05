
from ej14_decla import *

# dni=dnivalido()

dni = input("ingrese su dni: ")

esvalido=dnivalido(dni)

if esvalido == True:
    print ("El ingreso del dni es correcto")
