from vehiculo import Vehiculo
from auto import Auto
from camion import Camion
from moto import Moto


class Carrera:

    pista = []
    metros = 100

    def addVehiculo(self, vehiculo):
        self.pista.append(vehiculo)

    def comenzar(self):
        if self.__tieneVehiculo:
             for _ in range(self.metros):
                for i in range(len(self.pista)):
                    vehiculo = self.pista[i];  
                    if vehiculo.ver_litros() < 0:
                      del self.pista[i]      
                    vehiculo.avanzar()   

        else:
            print ("La pista no tiene Vehiculos")

    def __tieneVehiculo(self):
        return self.pista.len > 0

    def verGanadores(self):
        return self.pista


