# CONBINAR DICCIONARIOS con el método update
# Dados los diccionarios
# libros1 = {'LibroA': 1, 'LibroB': 2, 'LibroC': 3}
# libros2 = {'LibroC': 2, 'LibroD': 4, 'LibroE': 5}
# Conbina usando el método "update" y muestra su combinación en pantalla
# Pregunta: importa el orden de combinación?
# si importa el orden

libros1 = {'LibroA': 1, 'LibroB': 2, 'LibroC': 3}
libros2 = {'LibroC': 2, 'LibroD': 4, 'LibroE': 5}

libros1.update(libros2)

print(libros1)

