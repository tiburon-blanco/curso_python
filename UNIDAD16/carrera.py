class Carrera:
    def __init__(self):
        self.pista = int(
            input("ingrese la cantidad de metros que correran los vehiculos: ")
        )
        self.cantidad = int(input("Agrege que cantidad de vehiculos correran: "))
        print(
            " Se correra una carrera de: ",
            self.pista,
            "metros. Y participaran: ",
            self.cantidad,
            "de vehiculos.",
        )

    def tipos(self):
        lista = 0
        for _ in range(self.cantidad):
            seleccione = input("ingrese si es un camion, auto o moto: ")
            if seleccione == "auto" or "camion" or "moto":
                marca = input("ingrese marca: ")
                color = input("ingrese color: ")
                litros = int(input("ingrese la cantidad de litros: "))

            lista.append(seleccione)


mouras = Carrera()

print(mouras.cantidad)

lista = mouras.tipos
