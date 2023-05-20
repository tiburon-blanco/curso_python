import json

agenda = {}

file_name = 'data.txt' 


def obtenerAgenda(): 
    f = open(file_name,'r')
    data = f.read()
    f.close()
    return eval(data)

def agregar(number, name): 
    a = obtenerAgenda()
    a[number] = name
    f = open(file_name,'w')
    f.write(str(a))
    f.close()