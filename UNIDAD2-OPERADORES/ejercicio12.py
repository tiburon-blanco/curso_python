# Una ferretería vende clavos y tornillos,
# El precio de los clavos es de 0.7 c/u y el de los tornillos de es 1.25 c/u
# Escribir un programa que simule 2 ventas, preguntado al cliente cuantos clavos y tornillos necesita.
# Mostrar al final la cantidad de clavos y tornillos vendidos y monto recaudado para cada caso.

precio_C=float(0.7)
precio_T=float(1.25)

demanda_C=int(input("Ingrese la cantidad de clavos: "))
demanda_T=int(input("Ingrese la cantidad de tornillos: "))

clavos_total=float(demanda_C*precio_C)
tornillos_total=float(demanda_T*precio_T)

compra_T=clavos_total+tornillos_total

print("El valor de la compra de clavos es de pesos:",clavos_total)
print("El valor de la compra de tornillos es de pesos:",tornillos_total)
print("El valor total de la compra de clavos y tornillos asciende a la suma de pesos: ",compra_T)