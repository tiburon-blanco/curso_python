# WHILE
# Se ingresan por teclano números y se van mostrando en pantalla
# Hasta que se ingrese un 0


i=0

x=int(input("ingrese un numero por pantalla: "))

while True:
    if x == i:
        print("numero correcto: ")
        break
    else:
        print("Ingreso el numero equivocado, por favor:")
        x=int(input("ingrese un numero por pantalla: "))


print("Ingreso el numero correcto, que es cero")