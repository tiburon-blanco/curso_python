from maquina import Maquina


class Auto(Maquina):
    def avanzar(self):
        self.avanzar = True

    def consumo(self, litros):
        self.consumo = litros * 10
        print(
            "Este Auto con la cantidad de litros que posee puede recorrer: ",
            self.consumo,
            " ,metros.",
        )


auto = Auto("vw", "azul", 10)

print(auto.color, auto.marca, auto.litros)

print(auto.consumo(auto.litros))
