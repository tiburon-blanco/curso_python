# un mismo objeto podria cambiar de forma y por lo tanto sus funciones

class Auto():

    def desplazamiento(self):
        print("Me dezplazo utilizando cuatro 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me dezplazo utilizando dos 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me dezplazo utilizando seis 6 ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Auto()

# miVehiculo.desplazamiento()

# miVehiculo2 = Auto()

# miVehiculo2.desplazamiento()

# miVehiculo3 = Camion()

# miVehiculo3.desplazamiento()

desplazamientoVehiculo(miVehiculo)
