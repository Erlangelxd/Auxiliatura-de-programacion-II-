class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
    def mostrar(self):
        return f"El perro se llama {self.nombre} es de raza {self.raza} y tiene {self.edad} años"
    def sonido(self):
        return f"Guau Guau Guau"

class Gato:
    def __init__(self, nombre, edad, raza):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
    def mostrar(self):
        return f"El gato se llama {self.nombre} es de raza {self.raza} y tiene {self.edad} años"
    def sonido(self):
        return f"Miau Miau Miau"
    
perro1=Perro("Max", 5, "Cachuchin")
gato1=Gato("Garfield", 5, "XD")
print(perro1.sonido())
print(gato1.sonido())


