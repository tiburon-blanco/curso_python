
lista_mayores=[]
lista_menores=[]



def ver_lista_mayores():
    return lista_mayores

def ver_lista_menores():
    return lista_menores

def agregar_mayor(nombre):
       lista_mayores.append(nombre)
       

def agregar_menores(nombre):
       lista_menores.append(nombre)
       
def ver_informe():
    cantidad_menores = len(lista_menores)
    cantidad_mayores = len(lista_mayores)
    if cantidad_mayores > cantidad_menores:
        return "mayores"
    if cantidad_mayores < cantidad_menores:
        return "menores"
    if cantidad_mayores == cantidad_menores:
        return "iguales"





