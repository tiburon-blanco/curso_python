# Crear una funcion que valide un EMAIL
# Solicitar al usuario que ingrese su dirección email.
# Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo.
# Una dirección se considerará válida si contiene el símbolo "@".

# email=str(input("ingrese su correo electronico para verificar su validez: "))
# correo=email

# if "@" in email:
#     print("el correo es valido")
# else:
#     print("el correo es invalido, ingrese nuevamente: ")

email=input("ingrese su correo electronico para verificar su validez: ")
correo=email

def validacioncorreo(correo):
    if "@" in email:
        print("el correo es valido")
    else:
        print("el correo es invalido, ingrese nuevamente: ")
        
     
validacioncorreo(correo)



# validacion=True

# def validacioncorreo(email):
#     while validacion:
#         if "@" not in email:
#             print("el correo es invalido, ingrese nuevamente:")
            
#         if "@" in email:
#             print("el correo es valido")
#             validacion=False
            
     
# validacioncorreo(email)


