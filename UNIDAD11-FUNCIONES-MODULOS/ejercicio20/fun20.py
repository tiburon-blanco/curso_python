def superposicion_1(lista1,lista2):

	lista1 = lista1.split()
	lista2 = lista2.split()
	resu = set(lista1).intersección(lista2)
	if len(resu) > 0:
		return True


def superposicion_2(lista_1, lista_2):
    for i in lista_1:
        for x in lista_2:
            if i == x:
                print("La lista 1 contiene el mismo elemennto que la lista 2 y es: ", i)