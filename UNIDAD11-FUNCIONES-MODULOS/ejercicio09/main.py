# Se le pide al usuario que ingrese una letra
# Crear un funcion que cuenta la cantidad de letras que aparecen el el siguiente texto:

############################################################################################################
# Pinocchio cuenta la historia en acción real de una marioneta de madera que sueña con ser un niño de verdad. 
# Cuando Pinocchio consigue su deseo es feliz, pero es proclive a decir mentiras, 
# por lo que la consecuencia de ser humano es que su nariz crece y crece cada vez que miente.
# Es una historia que cuenta la relación que se da entre un padre y un hijo, 
# las consecuencias de mentir y la creación de historias en un mundo de fantasía.
############################################################################################################
texto= ("Pinocchio cuenta la historia en acción real de una marioneta de madera que sueña con ser un niño de verdad. Cuando Pinocchio consigue su deseo es feliz, pero es proclive a decir mentiras,  por lo que la consecuencia de ser humano es que su nariz crece y crece cada vez que miente.Es una historia que cuenta la relación que se da entre un padre y un hijo, las consecuencias de mentir y la creación de historias en un mundo de fantasía.")

letra= str(input("ingrese una letra: "))

def contarletras(l1):

    letra=l1
    if l1 in texto:
        return(texto.count(letra))

print("la letra aparece: ", contarletras(letra), " veces.")


    