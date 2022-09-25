# EXAMEN 1
# Se necesita desarrollar un sistema para un cajero de un supermercado.
# El sistema deberá procesar la ventas de las personas que se encuentren en la cola.
# y obtener información al final del proceso.
# El proceso de pago se hará de una persona por vez, donde, a cada una se le preguntará el nombre y
# se le procesarán los producto, así hasta el final de la cola.
# Cada persona puede comprar más de un producto.
# De cada producto se conoce su código, nombre y precio, la lista de productos es la siguiente:

# Codigo    - Nombre            - Precio
# 1640      - Mayonesa          - 100
# 1641      - Dulce de leche    - 120
# 1642      - Aceite            - 80
# 1643      - Pan               - 50
# 1644      - Fideos            - 75 
# 1645      - Galletitas        - 40
# 1646      - Cola Cola         - 160
# 1647      - Queso             - 200
# 1648      - Fanta             - 150   
# 1648      - Arroz             - 70
# 1650      - Mermelada         - 55

# El cajero debe preguntar a cada persona por el código del producto y la cantidad del producto que lleva.
# Si el producto no se encuentra dentro de la lista, se volverá a pedir el código nuevamente.
# Al finalizar el proceso (una vez procesada toda la cola de personas), se necesitará saber:

# A) La cantidad de personas atendidas.
# B) En nombre de la persona que más dinero gastó, junto con su monto.
# C) Cuál fue el producto más vendido.

# while para la cola / while para los productos
# A) Productos diccionario ( key: codigo // value Lista (nombre y precio))
# B) Variable o diccionario(nombre, productos)
# C) Diccionarios con codigo y cantidad.


productos={ 1640: ["Mayonesa",100], 
            1641: ["Dulce de lecha",120], 
            1642: ["Aceite",80], 
            1643: ["Pan",50], 
            1644: ["Fideos",75], 
            1645: ["Galletitas",40], 
            1646: ["Coca Cola",160], 
            1647: ["Queso",200], 
            1648: ["Fanta",150],
            1649: ["Arroz",70], 
            1650: ["Mermelada",55],
            }

contador_clientes=0

nombre_comprador=""
monto_compra_total=0

hay_cliente= True

tiene_producto=True

tiene_otro_producto=True

lista_compradores={}

prod_vendidos={}


# producto=["Aceite", 80]

while hay_cliente:
        nombre=input("ingrese el nombre del cliente: ")
        while tiene_producto:
            cod_prod=int(input("Que codigo de producto lleva: "))
            producto=productos[cod_prod]
            if producto is not None:
                cantidad=int(input("ingrese la cantidad de este producto que va a llevar: "))
                precio_producto= producto[1]
                monto_compra_prod=cantidad*precio_producto
                monto_compra_total=monto_compra_total + monto_compra_prod
                monto_esta_compra=0
                monto_esta_compra=monto_compra_prod
                prod_vendidos[cod_prod]=monto_compra_prod
                print ("El total de esta compra  hasta el momento es: ",monto_esta_compra)
                print ("El total de las compras acumuladas hasta el momento es: ",monto_compra_total)
            else:
              print("El codigo ingresado no existe, ingrese nuevamente")
            tiene_otro_producto=input("tiene algun otro producto: ")   
            if tiene_otro_producto=="NO":
                lista_compradores[nombre]=monto_esta_compra
                print(lista_compradores)
                print(prod_vendidos)
                contador_clientes= contador_clientes+ 1 
                print("El total de clientes hasta el momento es de: : ", contador_clientes)
                # recorrer diccionario de compradores y traer el que haya gastado mas
                # recorrer diccionario productos vendidos y traer el mayor
                break

print("El total de clientes hasta el momento es de: : ", contador_clientes)
print("")



    # clientes_en_fila=input("ingrese si hay mas gente en la fila SI O NO: " )
    # if clientes_en_fila==gente_esperando:
    #     print("Ingrese a la caja")
    # elif clientes_en_fila==sin_gente:
    #     seguir:False
       
        # while seguir:
        #     nombre=input("ingrese el nombre del cliente: ")
        #     cod_prod=int(input("Que codigo de producto lleva: "))       
        # if cod_prod in productos:
        #     cantidad=int(input("ingrese la cantidad de este producto que va a llevar: "))
        #     compra=compra+cantidad*100  # (multiplicar por segundo elemento del value de la lista)
        #     carrito=carrito+compra
        # if carrito==0:
        #     seguir=False
        
        # else:
        #      print("El codigo ingresado no existe, ingres nuevamente")            