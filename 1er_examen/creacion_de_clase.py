#Clase 1
class Persona:
    def __init__(self, nombre, edad, carrera):
        self.nombre=nombre
        self.edad=edad
        self.carrera=carrera
    def saludar(self):
        return f"Hola me llamo {self.nombre} tengo {self.edad} años y estudio {self.carrera}"
    def calular(self, numero1, numero2):
        suma= numero1+ numero2
        return f"El resultado es {suma}"
    
persona1=Persona("Jose", 20, "Ingenieria de sistemas")
persona2=Persona("Maria", 20, "Parvularia")
print(persona1.saludar())
print(persona2.saludar())
print(persona2.calular(50, 43))

#Clase 2
class Carro:
    def __init__(self, marca, color, numero_de_puertas, año):
        self.marca=marca
        self.color=color
        self.numero_de_puertas=numero_de_puertas
        self.año=año
        self.estado=False
        self.combustible=1
    def mostrar_datos(self):
        return f"La marca es {self.marca} \n de color {self.color} \n del año {self.año}"
    def encender(self):
        if self.estado == False:
            self.estado=True
            return f"Auto encendido"
        else:
            return f"El auto ya estaba encendido"
    def apagar(self):
        if self.estado == True:
            self.estado=False
            return f"Auto apagado"
        else:
            return f"El auto ya estaba apagado"
    def cargar_combustible(self, carga_combustible):
        #self.combustible = self.combustible + carga_combustible # Sirven igual pero es otra forma de escribir
        self.combustible += carga_combustible
    
auto1=Carro("Toyota", "Amarillo", 5, 1997)
auto2=Carro("Mercedez", "Blanco", 5, 2000)
# print(auto1.encender())
# print(auto1.encender())
# print(auto1.apagar())
print(auto1.mostrar_datos())
print(auto2.mostrar_datos())