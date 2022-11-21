def ingrese_tres_numeros():
    n1= int(input("ingrese el 1° numero: "))
    n2= int(input("ingrese el 2° numero: "))
    n3= int(input("ingrese el 3° numero: "))
    valores=[n1,n2,n3]
    return valores

def max_de_tres(valor):
    num_max=max(valor)
    return num_max