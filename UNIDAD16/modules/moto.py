from maquina import *


class Moto(Maquina):
    def consumo(self, litros):
        self.consumo = litros / 0.5 * 10
        print(
            "la autonomia de la moto con esta cantida de litros es de: ",
            self.consumo,
            "metros.",
        )


moto = Moto("vw", "azul", 10)

print(moto)
