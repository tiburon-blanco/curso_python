class Vehiculo:
    def __init__(self, piloto, marca, color, litros):
        self.piloto = piloto
        self.marca = marca
        self.color = color
        self.litros = litros

    def avanzar(self):
        self.avanzar = True

    def consumo(self):
        pass

    def ver_color(self):
        return self.color

    
    def ver_piloto(self):
        return self.piloto

    def ver_litros(self):
        return self.litros