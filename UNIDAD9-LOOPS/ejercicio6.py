# Dado la siguiente lista
# frutas = ["pera", "banana", "manzana", "uva", "mango", "kiwi", "melon", "frutilla", "naranja"]
# Agregar en OTRA lista aquellas frutas que tienen mas de 5 caracteres
# Al final imprimir en pantalla esa OTRA lista
# Recordar que con "append" se agregan elementos a una lista


frutas = ["pera", "banana", "manzana", "uva", "mango", "kiwi", "melon", "frutilla", "naranja"]

f_1=[]

for i in frutas:
    if len(i) > 5:
        f_1.append(i)

print(f_1)



       


