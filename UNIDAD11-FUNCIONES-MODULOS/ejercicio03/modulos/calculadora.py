
from modulos import operaciones

def calcular(oper, x,y):

    resultado = None

    if(oper == 1):
        resultado = operaciones.suma(x, y)
    if(oper == 2):
        resultado = operaciones.resta(x, y)
    if(oper == 3):
        resultado = operaciones.mult(x, y)
    if(oper == 4):
        resultado = operaciones.div(x, y)     

    return resultado     