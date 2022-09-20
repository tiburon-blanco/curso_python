# Escriba un programa donde se ingresen 2 palabras e imprima cual es la palabra que tiene mayor cantidad de caracteres
# OJO: avisar si la cantidad de carecteres de las palabras son iguales
# Ej: Si ingreso HOLA y PERRO, el programa debe responder: La palabra PERRO es la mayor y tiene 5 caracteres

palabra_1=input("Ingrese una palabra: ")
palabra_2=input("Ingrese otra palabra: ")

p1= (len(palabra_1))
p2= (len(palabra_2))

if p1==p2:
    print("Ambas palabras poseen la misma cantidad de caracteres")
else: 
    if p1>p2:
        print("La palabra: ", palabra_1, "es la mayor, ya que tiene: ", p1,  "caracteres")
    else:
        print("La palabra: ", palabra_2, "es la mayor, ya que tiene: ", p2,  "caracteres")




