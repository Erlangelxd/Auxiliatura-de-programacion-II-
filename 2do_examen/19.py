# def libros():
#     with open("libros.txt", "r") as archivo:
#         lineas = archivo.readlines()
#         for linea in lineas:
#             cod, titulo, autor, edicion , año = linea.strip().split(", ")





class Producto:
    def __init__(self, cod, titulo, autor, edicion , año):
        self.cod = cod
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.año = año

class Libro:
    productos="libros.txt"                #atributo 
    def __init__(self):
        with open (self.productos, "a"):
            pass
    def agregar(self, producto):
        with open(self.productos, "a") as archivo:
            archivo.write(f"{producto.cod}, {producto.titulo}, {producto.autor}, {producto.edicion}, {producto.año} \n")
    def leer_productos(self):
        with open(self.productos, "r") as archivo:
            lineas = archivo.readlines()
        return [linea.strip().split(",")
                for linea in lineas
                ] 
    def eliminar(self, nombre):
        product = self.leer_productos()
        with open (self.productos, "w") as archivo:
            for i in product:
                if i[0] != nombre:
                    archivo.write(", ".join(i) + "\n")
    def actualizar(self, nombre, nuevo_precio):
        product = self.leer_productos()
        with open(self.productos, "w") as archivo:
            for i in product:
                if i[0] == nombre:
                    i[1] = str(nuevo_precio)
                    archivo.write(", ".join(i) + "\n")

    def eliminarLibro(self):
        product = self.leer_productos()
        with open (self.productos, "w") as archivo:
            for i in product:
                if int(i[4]) > 1990:
                    archivo.write(",".join(i) + "\n")
    def actualizar_autor(self):
        product = self.leer_productos()
        with open(self.productos, "w") as archivo:
            for i in product:
                if i[2] == "Anonimo":
                    i[2] =  "Sin nombre"
                    archivo.write(", ".join(i) + "\n")
                

prod=Producto(1, "Cien años de soledad", "Garcia Marquez", "IV" , 2025)
prod2=Producto(2, "Viaje al centro de la tierra", "Julio Berne", "III" , 1989)
libros = Libro()
# libros.agregar(prod)
# libros.agregar(prod2)
# libros.eliminarLibro()
libros.actualizar_autor()