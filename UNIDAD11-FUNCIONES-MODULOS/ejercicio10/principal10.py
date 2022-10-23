def registro_usuario():

    nombre= input("Ingrese su nombre: ")
        
    apellido=input("ingrese su primer apellido: ")
        
    dni=input("ingrese su numero de Documento: ")
    
    datos = { "nombre": nombre, "apellido": apellido, "DNI": dni } 

    return datos


def crear_identificador(dato):
    # Martin 8 308
    id1 = dato["nombre"]

    id2 = str(len(dato["apellido"]))

    id3 = dato["DNI"][0:3]

    return id1 + id2 + id3

dato = registro_usuario()

identificador = crear_identificador(dato)

print(identificador)