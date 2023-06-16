class Coche():
    def __init__(self):
        self.largo = 250
        self.ancho = 160
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "el coche esta en marcha"

        elif (self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"

        else:
            return "El coche esta parado."

    def estado(self):
        print("el coche tiene", self.__ruedas, "ruedas. Un ancho de ",
              self.ancho, " y un lardo de ", self.largo)

    def get_ruedas(self):
        return self.__ruedas

    # def set_ruedas(self, ruedas):
    #     self.__ruedas = ruedas

    def __chequeo_interno(self):

        print("realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "mal"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):

            return True

        else:
            return False

    def asa(self):
        return


miCoche = Coche()

print("el largo del coche es: ", miCoche.largo)

print("El coche tiene: ", miCoche.get_ruedas(), "ruedas.")


print(miCoche.arrancar(True))

miCoche.estado()


print(".............A continuacion creamos el segundo objeto___________________")

miCoche2 = Coche()

print("el Largo del coche es: ", miCoche2.largo)
print("El coche tiene: ", miCoche2.get_ruedas(), "ruedas.")

print(miCoche.arrancar(False))

# miCoche2.__ruedas = 2

miCoche2.estado()
