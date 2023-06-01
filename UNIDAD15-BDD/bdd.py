import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

# miCursor.execute(
#     "CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(50))")

# variosProductos = [

#     ("Camiseta", 10, "deportes"),
#     ("Jarron", 90, "ceramica"),
#     ("Camiom", 20, "jugueteria"),

# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

print(variosProductos)


miConexion.commit()

miConexion.close()
