from maquina import Maquina
from auto import Auto
from camion import Camion
from moto import Moto


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
        lista = []
        for _ in range(self.cantidad):
            seleccione = input("ingrese si es un camion, auto o moto: ")
            if seleccione == "auto":
                marca = input("ingrese marca: ")
                color = input("ingrese color: ")
                litros = int(input("ingrese la cantidad de litros: "))
                objeto = Auto(marca, color, litros)
                lista.append(objeto)
            elif seleccione == "camion":
                marca = input("ingrese marca: ")
                color = input("ingrese color: ")
                litros = int(input("ingrese la cantidad de litros: "))
                objeto = Camion(marca, color, litros)
                lista.append(objeto)
            elif seleccione == "moto":
                marca = input("ingrese marca: ")
                color = input("ingrese color: ")
                litros = int(input("ingrese la cantidad de litros: "))
                objeto = Moto(marca, color, litros)
                lista.append(objeto)
            else:
                print("Tipo inválido, se omitirá este vehículo.")
                continue

            print(lista)
            return lista


mouras = Carrera()


mouras.tipos()
