from maquina import Maquina


class Camion(Maquina):

    def avanzar(self):
        pass

    def consumo(self, litros):
        self.consumo = litros/2 * 10
        print("La autonomia del camion con la cantidad de litros que posee es de: ", self.consumo)


camion = Camion("vw", "azul", 10)
