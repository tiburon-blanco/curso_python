# instrucciones Super


class Persona():

    def __init__(self, nombre, edad, Lugar_residencia):

        self.nombre = nombre

        self.edad = edad

        self.lugar_residencia = Lugar_residencia

    def descripcion(self):

        print("Nombre: ", self.nombre, "Edad: ", self.edad,
              "Residencia: ", self.lugar_residencia)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_emplado, edad_empleado, residencia_empleado):

        super().__init__(nombre_emplado, edad_empleado, residencia_empleado)

        self.salario = salario

        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()

        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)


Antonio = Persona("Antonio", 55, "España")

Antonio.descripcion()

Leo = Persona("Leo", 55, "Colombia")

Manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")

Manuel.descripcion()


# PRINCIPIO DE SUSTITUCION---- ES SIEMPRE UN/A ---- funcion isintance()


print(isinstance(Manuel, Persona))

print(isinstance(Manuel, Empleado))

print(isinstance(Leo, Empleado))
