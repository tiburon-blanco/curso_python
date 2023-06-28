from UNIDAD16POO.modules.maquina import Maquina


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
