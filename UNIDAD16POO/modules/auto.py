from maquina import Maquina


class Auto(Maquina):

    def avanzar(self):
        self.avanzar = True

    def consumo(self, litros):
        self.consumo = litros/2 * 10


auto = Auto("vw", "azul", 10)

print(auto)
