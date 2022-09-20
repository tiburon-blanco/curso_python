# Acabas de pedir un préstamo al banco por 3 meses.
# Al banco le debes pagar todos los meses la cuota. (La cuota es la cantidad de dinero que pediste / 3)
# El banco de cobra un interés de 8% por mes (de lo que te falta pagar)
# Escribir un programa que ingreses el monto del préstamo y muestre los pagos de las cuotas y la suma de interés total pagado

from tkinter import X

prestamo=100
meses=3
interes=8/100 # sobre saldo

monto=prestamo
plazo=meses

cuotas=int(monto/plazo)
saldo_1=monto-cuotas
saldo_2=saldo_1-cuotas

cuota_1=cuotas+monto*interes
cuota_2=cuotas+saldo_1*interes
cuota_3=cuotas+saldo_2*interes

monto_devuelto=cuota_1+cuota_2+cuota_3

print("el valor del prestamo es de pesos: ", monto)
print("su plazo de devolucion es de meses: ", plazo)
print( "El valor de cada cuota es de pesos: ", cuotas, " mas el interes del 8 porcentual sobre saldo")
print("La cuota 1 asciende a la suma de pesos: ", cuota_1,"este valor incluye el capital e interes sobre saldo.")
print("La cuota 2 asciende a la suma de pesos: ", cuota_2,"este valor incluye el capital e interes sobre saldo.")
print("La cuota 3 asciende a la suma de pesos: ", cuota_3,"este valor incluye el capital e interes sobre saldo.")
print("El valor total que se termina devolviendo es de pesos: ",monto_devuelto )



