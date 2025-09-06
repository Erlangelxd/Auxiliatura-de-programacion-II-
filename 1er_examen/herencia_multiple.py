class Animal:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    def hacer_sonido(self):
        pass
    def comer(self):
        return f"{self.nombre} está comiendo"
class Perro(Animal):
    def __init__(self, nombre, edad, genero, raza, tamaño):
        super().__init__(nombre, edad, genero)
        self.raza = raza
        self.tamaño = tamaño
    def hacer_sonido(self):
        return "Guau"
    def busqueda(self, objeto):
        return f"{self.nombre} está buscando {objeto}"
class xd(Animal):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)
class Gato(Animal):
    def __init__(self, nombre, edad, genero, color):
        super().__init__(nombre, edad, genero)
        self.color=color
    def hacer_sonido(self):
        return "Miau"
    def cazar(self, presa):
        return f"{self.nombre} está cazando {presa}"

class Mamifero:
    def __init__(self):
        self.tipo_de_pelo = "VERDE"
    def amamantar(self):
        return "El mamífero está amamantando a sus crías"
class Oviparo:
    def __init__(self):
        self.tipo_de_huevo = "Huevo con cáscara"
    def poner_huevos(self):
        return "El ovíparo está poniendo huevos"

class Ornitorrinco(Mamifero, Oviparo):
    def __init__(self, nombre):
        Mamifero.__init__(self)
        Oviparo.__init__(self)
        self.nombre = nombre
    def nadar(self):
        return f"{self.nombre} el ornitorrinco está nadando"

# perro1=Perro("Firulais", 3, "Macho", "Labrador", "Grande")
# gato1=Gato("Michi", 2, "Hembra", "Naranja")
# print(perro1.hacer_sonido())
# print(gato1.hacer_sonido())
# print(perro1.comer())

PERRY=Ornitorrinco("Perry")
print(PERRY.nadar())