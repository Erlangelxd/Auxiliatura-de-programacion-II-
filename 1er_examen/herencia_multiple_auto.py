class Auto_a_combustion:
    def __init__(self, marca, modelo, combustible):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
    def arrancar(self):
        return f"El auto {self.marca} {self.modelo} ha arrancado con {self.combustible}."
class Auto_electrico:
    def __init__(self, marca, modelo, bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
    def arrancar(self):
        return f"El auto {self.marca} {self.modelo} ha arrancado con batería de {self.bateria} kWh."

class Auto_hibrido(Auto_a_combustion, Auto_electrico):
    def __init__(self, marca, modelo, combustible, bateria, placa, año, color):
        Auto_a_combustion.__init__(self, marca, modelo, combustible)
        Auto_electrico.__init__(self, marca, modelo, bateria)
        self.placa = placa
        self.año = año
        self.color = color
    def arrancar(self):
        return f"El auto híbrido {self.marca} {self.modelo} ha arrancado con {self.combustible} y batería de {self.bateria} kWh."
    def piloto_automatico(self):
        return f"El auto híbrido {self.marca} {self.modelo} está en modo piloto automático."
auto_h1=Auto_hibrido("Toyota", "Prius", "gasolina", 8.8, "XDXD123", 2025, "Amarillo")
print(auto_h1.arrancar())