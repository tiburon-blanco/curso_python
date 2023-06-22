class Vehiculo():
    def __init__(self, marca, color, litros):
        self.marca = marca
        self.color = color
        self.litros = litros

    def avanzar(self, distancia):
        self.distancia_recorrida += distancia
        return

    def autonomia(self):
        return


class Auto(Vehiculo):
    def autonomia(self):
        return super().autonomia()


class Moto(Vehiculo):
    def autonomia(self):
        return super().autonomia()


class Camion():
    def autonomia(self):
