# La categoría de inmunización de COVID-19 se encuentra en la siguiente tabla:

#   Vacunas	    Inmunizacion

#   0	        Baja
#   1	        Media
#   2	        Alta
#   3	        Optima

# Escribir un programa que pregunte al usuario la cantidad de vacunas que tiene e indique su Inmunizacion

# Tenga en cuenta que el usuario puede indicar un valor fuera de las categorias indicadas, en ese caso indicar: Categoría inválida

print("categoría de inmunización de COVID-19")

baja=0
media=1
alta=2
optima=3

cantidad_vacuna=int(input("Ingrese la cantidad de vacunas que tiene: "))

if cantidad_vacuna==baja:
    print("Su categoría de inmunización de COVID-19 es baja")
elif cantidad_vacuna==media:
    print("Su categoría de inmunización de COVID-19 es media")
elif cantidad_vacuna==alta:
    print("Su categoría de inmunización de COVID-19 es alta")
elif cantidad_vacuna==optima:
    print("Su categoría de inmunización de COVID-19 es optima")
else:
    print("El numero ingresado es incorrecto")


