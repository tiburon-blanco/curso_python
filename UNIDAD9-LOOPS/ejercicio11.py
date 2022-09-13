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




############## EL OCHO ##########################


n = [4,6,8,1,6,15,5,20]
seguir = True
index = 0
while seguir:

    value = n[index]
    print(value)
    if value > 7:
        seguir = False
    index = index + 1

