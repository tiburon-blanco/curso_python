# METODOS del tipos STRING

# isalnum()     : Verifica si es un texo alfanumero
# isalpha()     : Verifica si es un texo alfabético
# isdigit()     : Verifica si el string es dígito
# isdecimal()   : Verifica si el string es decimal
# islower()     : Verifica esta en minúscula
# isupper()     : Verifica esta en minúscula
# isnumeric()   : Verifica si el string es numérico
# join()        : Unir string
# title()       : Capitaliza un frase (Le pone mayuscula a la primera letra de cada palabra)
# startswith()  : Si una frase comenza con otra

# Hacer una ejemplo con cada uno


texto=input("ingrese una frase para comprobar si es alfanumerico: ")

x=texto.isalnum()
print("el texto ingresado ",texto, "es alfanumerico?", x )

texto1=input("ingrese una frase para comprobar si es alfabetico: ")
x1=texto1.isalpha()
print("el texto ingresado ",texto1, "es alfabetico?", x1)

texto2=input("ingrese una frase para comprobar si es digito: ")
x2=texto2.isdigit()
print("el texto ingresado ",texto2, "es digito?", x2)


texto3=input("ingrese una frase para comprobar si es decimal: ")
x3=texto3.isdecimal()
print("el texto ingresado ",texto3, "es decimal?", x3)

texto4=input("ingrese una frase para comprobar si posee minusculas: ")
x4=texto4.islower()
print("el texto ingresado ",texto4, "esta en minuscula?", x4)

texto5=input("ingrese una frase para comprobar si posee mayusculas: ")
x5=texto5.isupper()
print("el texto ingresado ",texto5, "esta en mayuscula?", x5)

texto6=input("ingrese una frase para comprobar si es numerico: ")
x6=texto6.isnumeric()
print("el texto ingresado ",texto6, "es numerico?", x6)

nombres=["Leo, Jora, cefe, mansilla"]

print(nombres)

unir_nombres=",".join(nombres)
print(unir_nombres)

frase=input("ingrese una frase para capitalizar: ")

capitalizo=frase.title()
print(capitalizo)

ejerc_starwi=" Aprendiendo a programar en Python"
print(ejerc_starwi)
print(ejerc_starwi.startswith("Aprendiendo"))