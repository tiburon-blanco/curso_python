# Una verduleria tiene ofertas de Banana y Frutilla
# El precio del kilo de banana es de 100 y el de frutilla 120.
# La mercaderia se vende por kilo y solo puede llevar un tipo de fruta.

# OFERTA DE BANANA

# KG	    DESCUENTO
# 1	        0%
# 2	        10%
# 3 o mas	20%


# OFERTA DE FRUTILLA

# KG	    DESCUENTO
# 1	        5%
# 2	        15%
# 3 o mas	25%

# Escribir un programa que pregunte al usuario que tipo de fruta quiere y su cantidad (por kg) e informe el precio que tiene que pagar

print("Ofertas de Banana y Frutilla")
print("La mercaderia se vende por kilo y solo puede llevar un tipo de fruta")

fruta_1="banana"
fruta_2="frutilla"

p_banana=100
desc_ban_1kg= 0
desc_ban_2kg= 90/100
desc_ban_3kg= 80/100



p_frutilla=120
desc_frut_1kg= 95/100
desc_frut_2kg= 85/100
desc_frut_3kg= 75/100


fruta=input("Ingrese que tipo de fruta quiere: ")
kg=int(input("ingrese que cantidad en kg quiere: "))

if fruta != fruta_1 and fruta != fruta_2:
    print("Esta fruta no esta dentro de las promociones")


if fruta_1 == fruta:
    if kg==1:
        print("El precio del kg de banana es: ", p_banana*kg)
    if kg==2:
        print("El precio del kg de banana es: ", p_banana*kg*desc_ban_2kg)   
    if kg>=3:
        print("El precio del kg de banana es: ", p_banana*kg*desc_ban_3kg)

elif fruta_2 == fruta:
    if kg==1:
        print("El precio del kg de frutilla es: ", p_frutilla)
    if kg==2:
        print("El precio del kg de frutilla es: ", p_frutilla*kg*desc_frut_2kg)   
    if kg>=3:
        print("El precio del kg de frutilla es: ", p_frutilla*kg*desc_frut_3kg)     
else:
        print("debe ingresar alguna de las dos frutas en ofertas")



