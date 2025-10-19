class Vehiculo:
    def __init__(self, modelo, marca, color, año):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.año = año
    def mostrar(self):
        return f"Modelo: {self.modelo}, Marca: {self.marca}, Color: {self.color}, Año: {self.año}" 

class Auto(Vehiculo):
    def __init__(self, modelo, marca, color, año, volumen_gasolina):
        super().__init__(modelo, marca, color, año)
        self.volumen_gasolina = volumen_gasolina
        self.__tope_gasolina = 6
        self.__estado=False

    def get_tope_gasolina(self):
        return self.__tope_gasolina

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado=estado

    def cargar_gasolina(self, carga):
        self.volumen_gasolina += carga
        if self.volumen_gasolina >= self.get_tope_gasolina(): 
            self.volumen_gasolina = 6
            print("El tanque de gasolina está lleno")
        

    def encender(self):
        if self.get_estado() == True:
            print("El auto ya estaba encendido")
        else:
            self.set_estado(True)
            print("El auto se ha encendido")

    def apagar(self):
        if self.get_estado() == False:
            print("El auto ya estaba apagado")
        else:
            self.set_estado(False)
            print("El auto se ha apagado")
    def mostrar(self):
        return f"Nombre: {self.modelo}, Marca: {self.marca}, Color: {self.color}, Año: {self.año}, Volumen de gasolina: {self.volumen_gasolina}L, el auto esta {self.get_estado() and 'encendido' or 'apagado'}"

auto1 = Auto("Sedan", "Toyota", "Rojo", 2020, 2)
print(auto1.mostrar())  
auto1.encender()
auto1.apagar()
print(auto1.mostrar())  
print(auto1.mostrar())
auto1.cargar_gasolina(2)
auto1.cargar_gasolina(2)
auto1.cargar_gasolina(2)
print(auto1.mostrar())