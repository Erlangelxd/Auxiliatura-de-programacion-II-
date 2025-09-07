class Planta:
    def __init__(self, nombre, tipo, tamaño):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
    def fotosintesis(self):
        return f"La planta {self.nombre} está realizando la fotosíntesis"
    def crecer(self):
        return f"La planta {self.nombre} está creciendo"
class Girasol(Planta):
    def __init__(self, nombre, tipo, tamaño, flor):
        super().__init__(nombre, tipo, tamaño)
        self.flor=flor
    def seguir_sol(self):
        return f"La {self.nombre} está siguiendo al sol"
    def crecer(self):
        if self.tamaño >= 2:
            self.tamaño = 2
            return f"La planta {self.nombre} ha alcanzado su tamaño máximo de {self.tamaño} metros"
        else:
            self.tamaño+=0.5
        return f"La planta {self.nombre} ha crecido a {self.tamaño} metros"

planta1=Girasol("Girasol", "Boliviana", 1, True)
print(planta1.fotosintesis())
print(planta1.crecer())
print(planta1.crecer())
print(planta1.crecer())