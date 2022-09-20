# WHILE
# Se ingresan por teclano números y se van mostrando en pantalla
# Hasta que se ingrese un 0


i=0



while True:
    x=int(input("ingrese un numero por pantalla: "))
    if x == i:
        print("numero correcto: ")
        break
    else:
        print("Ingreso el numero equivocado, por favor:")
        

print("Ingreso el numero correcto, que es cero")