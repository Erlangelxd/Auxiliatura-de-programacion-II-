class ProductoElectronico:
    def __init__(self, nombre:str, marca:str, precio:float):
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
    def mostrar(self):
        return f"Nombre: {self.nombre}, marca: {self.marca}, precio: {self.precio}"
    
class Televisor(ProductoElectronico):
    def __init__(self, nombre, marca, precio, tamaño, tipo):
        super().__init__(nombre, marca, precio)
        self.__tamaño=tamaño
        self.__tipo=tipo
    def getTamaño(self):
        return self.__tamaño
    def setTamaño(self, newTamaño):
        self.__tamaño=newTamaño
    def getTipo(self):
        return self.__tipo
    def setTipo(self, newTipo):
        self.__tipo=newTipo
    def mostrar(self):
        return f"Nombre: {self.nombre}, marca: {self.marca}, precio: {self.precio}, Tamaño: {self.getTamaño()}, Tipo: {self.getTipo()}"

class Refrigerador(ProductoElectronico):
    def __init__(self, nombre, marca, precio, capacidad, color):
        super().__init__(nombre, marca, precio)
        self.__capacidad=capacidad
        self.__color=color
    def getCapacidad(self):
        return self.__capacidad
    def setCapacidad(self, newCapacidad):
        self.__capacidad=newCapacidad
    def getColor(self):
        return self.__color
    def setColor(self, newColor):
        self.__color=newColor
    def mostrar(self):
        return f"Nombre: {self.nombre}, marca: {self.marca}, precio: {self.precio}, capacidad: {self.getCapacidad()}, Color: {self.getColor()}"
class Licuadora(ProductoElectronico):
    def __init__(self, nombre, marca, precio, potencia, nro_de_piezas):
        super().__init__(nombre, marca, precio)
        self.__potencia=potencia
        self.__nro_de_piezas=nro_de_piezas
    def getPotencia(self):
        return self.__potencia
    def setPotencia(self, newPotencia):
        self.__potencia=newPotencia
    def getNro_de_piezas(self):
        return self.__nro_de_piezas
    def setNro_de_piezas(self, newNro_de_piezas):
        self.__nro_de_piezas=newNro_de_piezas
    def mostrar(self):
        return f"Nombre: {self.nombre}, marca: {self.marca}, precio: {self.precio}, potencia: {self.getPotencia()}, Piezas: {self.getNro_de_piezas()}"
    

tv=Televisor("TV", "LG", 6000, 64, "SmartTV")
tv2=Televisor("TV2", "LG", 2000, 100, "Normal")
refri=Refrigerador("Refrigerador", "Daewo", 10000, 5, "Negro")
licuadora=Licuadora("Licuadora", "Oster", 2000, 6000, 10)
productos=[tv, tv2, refri, licuadora]
def verificarMarca():
    for i in range (len(productos)):
        print(productos[i].mostrar())
        try:
            if productos[i].marca == productos[i+1].marca:
                print("marcas repetidas")
            else:
                print("x")
        except IndexError:
            pass
verificarMarca()
productosPrecio=[tv.precio, tv2.precio, refri.precio, licuadora.precio]
def verificarPrecio():
    maxprecio=productosPrecio[1]
    for i in range(len(productosPrecio)):
        if maxprecio <= productosPrecio[i]:
            maxprecio = productosPrecio[i]
    print(maxprecio)
verificarPrecio()