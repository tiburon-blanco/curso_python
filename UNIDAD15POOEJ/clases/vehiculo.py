class Vehiculo():
    def __init__(self, marca, color, litros):
        self.marca = marca
        self.color = color
        self.litros = litros

    def avanzar(self):
        pass

    def consumo(self):
        pass
    
    def ver_color(self):
        return self.color