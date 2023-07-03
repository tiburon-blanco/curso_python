from vehiculo import Vehiculo


class Camion(Vehiculo):

    litro_por_metro = 2

    def avanzar(self):
        self.litros = self.litros - self.litro_por_metro
