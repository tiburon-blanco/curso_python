# WHILE
# Data la siguiente lista:
# n = [4,6,8,1,6,15,5,20]
# Recorrer con WHILE hasta que encuentre un número mayor a 10

n = [4,6,8,1,6,15,5,20]

seguir = True
index = 0

while seguir:
    value = n[index]
    if value > 10:
        print(value)
        seguir= False
    index = index + 1

    


        