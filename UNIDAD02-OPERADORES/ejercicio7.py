# Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.
# un pie son doce pulgadas y una pulgada son 2,54 cm.
pulgada=2.54
pie=12*pulgada

distancia_1=float(input("ingrese la distancia en pies: "))
distancia_2=float(input("ingrese la distancia en pulgadas: "))


dist_cm=(distancia_1*(pulgada*12))+(distancia_2*pulgada)

print("La conversion de pies y pulgadas es de", dist_cm, "centimetros")