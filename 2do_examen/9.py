# 9. Dado la clase hija JefePolicia con las clases padres Persona, Empleado, Policia. Se pide:
# a) Identificar en cada clase 2 atributos significativos y crear 2 objetos de la clase hija y mostrar sus datos.
# b) Mostrar el nombre de aquel que tiene mayor sueldo.
# c) Comparar si ambos tienen mismo grado
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        pass
class Empleado:
    def __init__(self, salario, puesto):
        self.salario=salario
        self.puesto=puesto
        pass
class Policia:
    def __init__(self, rango, antiguedad):
        self.rango=rango
        self.antiguedad=antiguedad
        pass

class JefePolicia(Persona, Empleado, Policia):
    def __init__(self, nombre, edad, salario, puesto, rango, antiguedad):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, salario, puesto)
        Policia.__init__(self, rango, antiguedad)
    def mostrarDatos(self):
        return f"{self.nombre}, {self.antiguedad}"

b1=JefePolicia("Alex", 44, 7000, "General", "II", 5)
b2=JefePolicia("Alan", 44, 10000, "General", "II", 10)
if b1.salario > b2.salario:
    print(f"{b1.nombre} gana mas que {b2.nombre}")
else:
    print(f"{b2.nombre} gana mas que {b1.nombre}")

if b1.rango == b2.rango:
    print("rangos iguales")
else:
    print("rangos distintos")