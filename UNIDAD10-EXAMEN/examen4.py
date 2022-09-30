precio_pato=200
precio_gallina=100
precio_chancho=500

cantidad_animales=0 
venta_pato = venta_gallina = venta_chancho =0
stock_pato = stock_gallina = stock_chancho=0
venta= True
hay_cliente=True

monto_total_pato = monto_total_gallina = monto_total_chancho = 0
dias=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
tipo_animal = ['P', 'G', 'C']

for i in range(5):
    print("DIA:", dias[i])
    stock_pato = stock_pato + int(input("Ingrese el stock de patos del dia:  " +  dias[i]))
    stock_gallina = stock_gallina + int(input("Ingrese el stock de gallinas del dia:  " +  dias[i]))
    stock_chancho = stock_chancho + int(input("Ingrese el stock de chanchos del dia:  " + dias[i]))

    while hay_cliente:
        hay_cliente = input("ingrese S/N si hay o no clientes: ")
        if hay_cliente =="S":
            venta=True
            while venta:
                tipo = ''
                tipo_animal_correcto = True
                while tipo_animal_correcto:
                    tipo = input("Que animal desea comprar: Pato (P), Gallina (G), Chancho (C): ")
                    tipo_animal_correcto = True if tipo not in tipo_animal else False
                    cantidad = int(input("Que cantidad necesita?"))
                    if tipo == 'P':
                        hay_stock = (stock_pato - cantidad) > 0
                        if hay_stock:
                            stock_pato = stock_pato - cantidad
                            precio = cantidad * precio_pato
                            monto_total_pato = monto_total_pato + precio
                            cantidad_animales = cantidad_animales + 1
                            print("El monto de su compra de patos es: ", precio)
                    if tipo == 'G':
                        hay_stock = (stock_gallina - cantidad) > 0
                        if hay_stock:
                            stock_gallina = stock_gallina - cantidad
                            precio = cantidad * precio_gallina
                            monto_total_gallina = monto_total_gallina + precio
                            cantidad_animales = cantidad_animales + 1
                            print("El monto de su compra de gallina es: ", precio)
                    if tipo == 'C':
                        hay_stock = (stock_chancho - cantidad) > 0
                        if hay_stock:
                            stock_chancho = stock_chancho - cantidad
                            precio = cantidad * precio_chancho
                            monto_total_chancho = monto_total_chancho + precio
                            cantidad_animales = cantidad_animales + 1
                            print("El monto de su compra de chanchos es: ", precio)
                        
                    compra=input("Desea hacer otra compra S/N:  ")
                    if compra == "N":  
                        venta ==False     
        else:
            hay_cliente: False
            

    
     
print("Cantidad de animales vendidos: ", cantidad_animales) 
print("Monto total Pato: ", monto_total_pato)
print("Monto total Gallina: ", monto_total_gallina)
print("Monto total Chancho: ", monto_total_chancho)
monto_total = monto_total_pato + monto_total_gallina + monto_total_chancho
print("Monto total: ", monto_total)

