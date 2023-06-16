class Vehiculo():
    def __init__(self, marca, color, litros):
        self.marca = marca
        self.color = color
        self.nasta = litros


Auto = Vehiculo("toyota", "rojo", 100)


print(Auto.marca, Auto.color, Auto.nasta)
