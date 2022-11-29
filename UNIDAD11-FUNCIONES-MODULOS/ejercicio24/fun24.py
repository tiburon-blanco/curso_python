
lista  = ["1","123456","1234567891"]

def  mas_larga (lista):
    mas_larga = " "
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga=i
        return mas_larga

print (mas_larga ( lista ))



	# for  palabra  in  lista :
	# 	if  palabra_mayor  <=  len ( palabra ):
	# 		palabra_mostrar  =  palabra
	# 		palabra_mayor  =  len ( palabra )
	# 	else:
    #         palabra_mostrar 

	# print ( palabra_mostrar )


print (mas_larga ( lista ))