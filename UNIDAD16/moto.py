from vehiculo import Vehiculo

class Moto(Vehiculo):

    litro_por_metro = 0.5

    def avanzar(self):
        self.litros = self.litros - self.litro_por_metro