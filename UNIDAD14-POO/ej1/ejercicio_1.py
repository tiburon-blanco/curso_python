class Coche():
    largo = 250
    ancho = 160
    ruedas = 4
    enmarcha = False

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if (self.enmarcha):
            return "el coche esta en marcha"

        else:
            return "El coche esta parado."


miCoche = Coche()


print("el alrgo del coche es: ", miCoche.largo)

miCoche.arrancar()

print(miCoche.estado())
