# En un bar dejan entrar a personas mayores de edad que tengan al menos 2 vacunas.
# El encargado del acceso debe valida esta información previamente.
# Escribir un programa para el encargado del bar que valide el acceso e indique si dejo o no entrar a la persona.
# Además indicar el motivo por el cual la persona no accede al bar (En caso que no acceda)

print("Para ingresar al bar debe ser mayor de edad y poseer dos vacunas")

edad_permititda=18
ingreso_vacunas=2

edad=int(input("Corrobere e ingrese la edad del cliente: "))
vacunas=int(input("corrobore e ingrese la cantidad de vacunas que posee el cliente: "))

if edad>=edad_permititda and vacunas>=ingreso_vacunas:
    print("Puede ingresar porque cumple con ambos requisitos")
elif  edad>=edad_permititda and vacunas<ingreso_vacunas:
    print("No puede ingresar porque no posee la cantidad de vacunas requeridas")
elif  edad<edad_permititda and vacunas>=ingreso_vacunas:
    print("No puede ingresar porque no es mayor de edad")

else:
    print("no cumple los requisitos legales y/o sanitarios de acceso al local")

