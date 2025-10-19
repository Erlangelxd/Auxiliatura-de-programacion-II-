# with open("estudiantes.txt", "w") as archivo: # Crea y escribe un archivo
#     archivo.write("Hola mundo")

with open("estudiantes.txt", "r") as archivo: # Lee el archivo
    contenido=archivo.read()
    print(contenido)

# with open("estudiantes.txt", "a") as archivo: # Agrega una linea nueva al archivo
#     archivo.write("\n Chao mundo")

with open("estudiantes.txt", "r") as archivo:
    for linea in archivo:
        print(linea[0:4])