# Se tiene la siguiente lista de productos

# productos={ 1001: ["Producto 1", 10 , 100], 
#             1002: ["Producto 2", 15 , 100],  
#             1003: ["Producto 3", 12 , 100], 
#             1004: ["Producto 4", 20 , 100], 
#             1005: ["Producto 5", 22 , 100], 
# }
# Diccionario con el código y el value un lista con:
# Nombre del producto
# Precio
# Stock
# 
# Llega los clientes y pueden "COMPRAR" o "DEVOLVER" el producto
# Cada cliente hace una acción y solo puede comprar 1 producto
# En cada caso (Compra o devolución) le dicen al vendedor el código del producto y la cantidad
# Crear 2 funciones "comprar" y "devolver" que le permita vender el producto, avisar si no hay stock

# Manejar la lista de productos y las funciones en otro módulo (Archivo)

# Existe producto booleano

# comprar  // # hay stock
# devolver

from productos import *

seguir=True
while seguir: 
    accion= input("Ingrese C si desea comprar o D si desea devolver: ")
    codigo = int(input("Ingrese el codigo del producto: "))
    cantidad = int(input ("ingrese la cantidad: "))

    if accion == "C":
        if existe_producto(codigo):
            if hay_stock(codigo, cantidad):
                producto=comprar(codigo, cantidad)
                monto= producto[1]*cantidad
                print("El valor de la compra de: ", producto[0],  " es de pesos", monto)

            else:
                print("no hay stock del producto solicitado.")
        else:
            print("El producto no existe.")

    elif accion == "D":
        if existe_producto(codigo):
            producto= devolver(codigo, cantidad)
            print("Gracias por devolver el producto: ", producto[0])

        else:
            print("No puede devolver ese producto porque no existe: ")

    else:
        print("Ingrese la accion correcta.")

    atender= input("desea atender otro cliente S/N: " )

    if atender != "S":
        seguir = False

print("Stock final: ")


p= ver_productos()


for i in p:
    producto = p[i]
    print ("el producto: ",  producto[0], "tiene stock de: ", producto[2], "cantidad.")
        