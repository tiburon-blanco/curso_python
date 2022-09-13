edades = [5, 14, 7, 23, 31, 5, 32, 19]
valor = int(input("Ingrese el valor a buscar: "))

#for index, edad in enumerate(edades):
#    if(edad == valor):
#        print(index)
#       break



pos = edades.index(valor)

otro = int(input("Ingrese otro valor a buscar: "))

edades[pos] = otro

print(edades)