# Dado el set
# frutas = {"pera", "banana", "manzana", "uva", "mango", "kiwi", "melon", "frutilla", "naranja"}
# Contar la cantidad de frutas que tienen menos de 5 caracteres


frutas = {"pera", "banana", "manzana", "uva", "mango", "kiwi", "melon", "frutilla", "naranja"}

for i in frutas:
    if len(i) < 5:
       print(i)