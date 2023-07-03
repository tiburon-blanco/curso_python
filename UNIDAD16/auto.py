from vehiculo import Vehiculo


class Auto(Vehiculo):

    litro_por_metro = 1

    def avanzar(self):
        self.litros = self.litros - self.litro_por_metro