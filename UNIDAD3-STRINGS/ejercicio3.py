# BUSCAR
# Ingrear por teclado 2 palabras, se deberá buscar la segunda palabra dentro de la primera e imprimir el resultado de find
# Que tipo de variable es?


frase=input("ingrese una frase: ")

palabra= input("ingrese una palabra: ")

resultado=frase.find(palabra)
print(type(resultado))
print(resultado)