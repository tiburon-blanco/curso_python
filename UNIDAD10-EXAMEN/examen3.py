# EXAMEN 3
# Horacio vive en el campo junto con su padre Carlos
# Se acerca fin de año y Horacio decide vender animales una semana antes de las fiestas.
# Los animales que venden son 3: patos, gallinas, y chanchos 
# Desarrollar un sistema que le permita a Horacio vender los animales durante 1 semana (5 dias L A V)
# Sabiendo que al inicio de cada día, su papá Carlos, le informa el stock diario con el que cuenta (Durante el dia)
# Procesar las ventas de toda la semana (L a V) para informar:
# 1) Cantidad de animales vendidos y su monto
# 2) Monto total de todas las ventas

# Tener en cuenta: 

# A: El stock es acumulativo.
# B: Cada comprador puede comprar más de una animal
# C: Se debe informar al comprador el monto de la compra
# D: Informar el comprador si no hay stock del animal que necesita
# E: Precio x unidad:
#    Pato = 200 pesos
#    Gallina = 100 pesos
#    Chancho = 500 pesos

precio_pato=200
precio_gallina=100
precio_chancho=500

ventas=0

venta_pato=0
venta_gallina=0
venta_chancho=0


venta= True

# for 1-5

while venta:
    stock_pato=int(input("ingrese el stock de patos a la venta que hay: "))
    stock_gallina=int(input("ingrese el stock de gallinas a la venta que hay: "))
    stock_chancho=int(input("ingrese el stock de chanchos a la venta que hay: "))
    compra_pato=input("Ingrese S/N si quiere comprar patos: ")
    if compra_pato.upper() == "S":
        cantidad_pato=int(input("ingrese la cantidad de patos que quiere: "))
        if cantidad_pato<=stock_pato:
            venta_pato=cantidad_pato*precio_pato
            stock_pato=stock_pato-cantidad_pato
            print("El monto de su compra de patos es: ", venta_pato)
        else:
            print("La cantidad demanda supera el stock, no puede comprar mas de: ", stock_pato)
    compra_gallina=input("Ingrese S/N si quiere comprar gallinas: ")
    if compra_gallina.upper() == "S":
        cantidad_gallina=int(input("ingrese la cantidad de gallinas que quiere: "))
        if cantidad_gallina<=stock_gallina:
            venta_gallina=cantidad_gallina*precio_gallina
            stock_gallina=stock_gallina-cantidad_gallina
            print("El monto de su compra de gallinas es: ", venta_gallina)
        else:
            print("La cantidad demanda supera el stock, no puede comprar mas de: ", stock_gallina)
    compra_chancho=input("Ingrese S/N si quiere comprar chanchos: ")
    if compra_chancho.upper() == "S":
        cantidad_chancho=int(input("ingrese la cantidad de chanchos que quiere: "))
        if cantidad_chancho<=stock_chancho:
            venta_chancho=cantidad_chancho*precio_chancho
            stock_chancho=stock_chancho-cantidad_chancho
            print("El monto de su compra de chancho es: ", venta_chancho)
        else:
            print("La cantidad demanda supera el stock, no puede comprar mas de: ", stock_chancho)
    hay_clientes=input("Si hay mas clientes ingrese: S/N: ")
    if hay_clientes.upper()== "N":
        venta=False



    print("el monto total de su compra es de: ", venta_pato + venta_gallina + venta_chancho, )

    print("lA cantidad de patos vendidos es de: ", cantidad_pato, "y el monto es de ", venta_pato)

    print("lA cantidad de gallinas vendidas es de: ", cantidad_gallina, "y el monto es de ", venta_gallina)

    print("lA cantidad de chanchos vendidos es de: ", cantidad_chancho, "y el monto es de ", venta_chancho)
    
    venta=False
    
    




    # compra_gallinas=input("Ingrese S/N si quiere comprar gallinas: ")
    # if compra_gallinas.upper() == "S":
    #     cantidad=int(input("ingrese la cantidad de gallinas que quiere: "))
    #     venta_gallina=cantidad*precio_gallina
    #     print("El monto de su compra de gallinas es es: ", venta_gallina)
    # compra_chanchos=input("Ingrese S/N si quiere comprar chanchos: ")
    # if compra_chanchos.upper() == "S":
    #     cantidad=int(input("ingrese la cantidad de chanchos que quiere: "))
    #     venta_chanchos=cantidad*precio_chancho
    #     print("El monto de su compra de chanchos es es: ", venta_chancho)
    
        

    # print("La cantidad de animales vendidos es venta pato/venta gallina / venta chancho")