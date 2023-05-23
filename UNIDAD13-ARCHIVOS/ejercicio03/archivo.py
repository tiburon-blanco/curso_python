from io import open

# se puede abrir un archivo en modo lectura/escritura/append

archivo_texto = open("archivoo.txt", "w")

frase = "barbaro, a ver si guarda algo. "

archivo_texto.write(frase)

archivo_texto.close()


archivo_texto = open("archivoo.txt", "r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto)
