class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

class Inventario:
    productos="inventario.txt"                #atributo 
    def __init__(self):
        with open (self.productos, "a"):
            pass
    def agregar(self, producto):
        with open(self.productos, "a") as archivo:
            archivo.write(f"{producto.nombre}, {producto.precio}, {producto.stock} \n")
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

# cantidad = int(input("Cantidad a agregar: "))
# for i in range(cantidad):
#     nombre = input("Nombre: ")
#     precio = input("Precio: ")
#     stock = input("Stock: ")
#     prod=Producto(nombre, precio, stock)
#     obj1=Inventario()
#     obj1.agregar(prod)

bj1=Inventario()
bj1.actualizar("Teclados", 500)