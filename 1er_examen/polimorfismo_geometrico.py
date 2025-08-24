#Polimorfismo con figuras geometricas
class Circulo:
    def __init__(self, radio):
        self.radio=radio
    def calcular_area(self):
        return 3.1416*(self.radio)**2
class Triangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        return (self.base*self.altura)/2

circulo1=Circulo(5)
triangulo1=Triangulo(4,5)
print(circulo1.calcular_area())
print(triangulo1.calcular_area())
