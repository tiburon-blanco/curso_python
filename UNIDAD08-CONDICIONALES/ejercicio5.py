# Escribir un programa calcule el IMC (Índice de masa corporal)
# Dado el peso y la altura por teclado, calcular IMC = Peso (kg) / altura (m)**2
# Ademas indicar:
# Si el IMC es menor a 18.5 debe indicar: Peso inferior al normal
# Si el IMC esta entre 18.5 – 24.9 debe indicar: Peso Norma
# Si el IMC esta entre 25.0 – 29.9 debe indicar: Peso superior al normal
# Si el IMC es mayor a 30.0 debe indicar: Obesidad

peso=float(input("ingrese peso: "))
altura=float(input("ingrese altura:"))
IMC=float(peso/(altura*2))
print("Su indice de masa corporal es: ",IMC)

if IMC<18.5:
    print("Peso inferior al normal")
if IMC>=18.5 and IMC<=24.9:
        print("Peso  normal")
if IMC>=25 and IMC<=29.9:
        print("Peso superior al normal")
if IMC>30:
        print("Obesidad")
   
