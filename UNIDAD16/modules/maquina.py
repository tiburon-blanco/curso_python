class Maquina:
    def __init__(self, marca, color, litros):
        self.marca = marca
        self.color = color
        self.litros = litros

    def avanzar(self):
        self.avanzar = True

    def consumo(self):
        pass

    def ver_color(self):
        return self.color


# class Pista():
#     def __init__(self, tipo, metros):
#         self.tipo = tipo
#         self.metros = metros


# class Carrera():
#     def __init__(self):

#     def agregar_vehiculos():

#     def inicio(self):


# pista = Pista("circular", 500)

# print("La pista es: ", pista.tipo,
#       "y posee un recorrido de: ", pista.metros, " metros")
