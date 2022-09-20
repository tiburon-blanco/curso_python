# Mostrar en pantalla la tabla de 5 de la siguietne manera:
# 5 X 0 = 0
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# ....

# (USAR FOR con ENUMERATE y RANGE para obtener el indice)



print("Ejerecicio utilizando la for")
value = 5
i = 0
     
for x in range(0,50,5):
    print(value, "X", i, "=", x)
    i= i + 1



print("Ejerecicio utilizando enumerate")
tabla=["5 X 0 = 0","5 X 1 = 5", "5 X 2 = 10", "5 X 3 = 15"]

for index, value in enumerate(tabla):
    print(value)
    

   
