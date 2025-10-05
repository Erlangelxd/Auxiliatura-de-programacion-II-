class Persona():
    def __init__(self):
        self.__nombre = "Erlan"
        self.__edad = 20
        self.__carrera = "Ingenieria de sistemas"
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def getEdad(self): # GET para que nos retorne el valor del atributo privado
        return self.__edad
    def setEdad(self, nueva_edad): # SET para modificar el valor del atributo privado
        self.__edad = nueva_edad
    def crecer(self):
        self.setEdad(self.getEdad()+1)
        print(f"{self.__nombre} ha crecido y ahora tiene {self.__edad} años")
    def __str__(self):
        return f"Hola me llamo {self.__nombre}, tengo {self.__edad} años y estudio {self.__carrera}"
p1= Persona()
p1.crecer()
p1.crecer()
print(p1)
