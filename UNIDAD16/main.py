from carrera import *

print("1- PREPARACION DE LA CARRERA____________")

carrera = Carrera()

seguir_cargando_vehiculo = 'S'
while seguir_cargando_vehiculo == 'S':
        
        while True:
            tipo_vehiculo = input("Seleccione el tipo de Vehiculo: A (Auto), M (Moto), C (Camion): ")
            if tipo_vehiculo == 'A' or tipo_vehiculo == 'M' or tipo_vehiculo == 'C':
                break

        piloto = input("Ingrese nombre del piloto: ")
        marca = input("Ingrese marca: ")
        color = input("Ingrese color: ")
        litros = int(input("ingrese la cantidad de litros: "))

        vehiculo = None
        if tipo_vehiculo == "A":
            vehiculo = Auto(piloto, marca, color, litros)
        if tipo_vehiculo == "M":
            vehiculo = Moto(piloto, marca, color, litros)
        if tipo_vehiculo == "C":
            vehiculo = Camion(piloto, marca, color, litros)

        carrera.addVehiculo(vehiculo)

        seguir_cargando_vehiculo = input("Desea agregar otro auto: (S/N)")


carrera.comenzar()
ganadores = carrera.verGanadores()
print(ganadores)

