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
hay_cliente= True
lista_compradores={}
prod_vendidos={}
b_monto_maximo_cliente=0
b_nombre_monto_maximo=""

while hay_cliente:
        nombre=input("ingrese el nombre del cliente: ")
        monto_esta_compra=0
        tiene_producto=True
        contador_clientes=contador_clientes+1
        while tiene_producto:
            cod_prod=int(input("Que codigo de producto lleva: "))
            if cod_prod in productos:
                producto=productos[cod_prod]
                cantidad=int(input("ingrese la cantidad de " + producto[0] + " que va a llevar: "))
                precio_producto= producto[1]
                monto_compra_prod=cantidad*precio_producto
                monto_esta_compra=monto_compra_prod+monto_esta_compra
                acumulados= prod_vendidos[cod_prod] if cod_prod in prod_vendidos else 0
                prod_vendidos[cod_prod]= acumulados + cantidad             
                print ("El total de esta compra  hasta el momento es: ",monto_esta_compra)
                tiene_otro_producto=input("Tiene algun otro producto (S/N): ")   
                if tiene_otro_producto.upper()=="N":
                    tiene_producto=False
                
            else:
                print("El codigo ingresado no existe, ingres nuevamente") 
        if  monto_esta_compra>b_monto_maximo_cliente:
            b_monto_maximo_cliente=monto_esta_compra
            b_nombre_monto_maximo= nombre

        hay_mas_clientes=input("Hay algun otro cliente? S/N")    
        if hay_mas_clientes.upper()== "N":
            hay_cliente=False


print("informe final")
print("A: la cantidad de personas atendidas es:", contador_clientes)
print("B: la persona que mas gasto es:", b_nombre_monto_maximo, " su monto fue de:", b_monto_maximo_cliente)

key_mayor_producto_vendido=0
value_mayor_producto_vendido=0
for key in prod_vendidos:
    value = prod_vendidos[key]
    if value > value_mayor_producto_vendido:
        key_mayor_producto_vendido=key
        value_mayor_producto_vendido = value


producto = productos[key_mayor_producto_vendido];
p = producto[0]
print("C: El producto mas vendido es:", p)

