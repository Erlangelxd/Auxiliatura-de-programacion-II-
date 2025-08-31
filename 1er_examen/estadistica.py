class Estadistica():
    def __init__(self, datos):
        self.datos=datos
    def muestra(self):
        return len(self.datos)
    def frecuencias(self):
        unicos = set(self.datos)
        for valor in sorted(unicos):
            print(f"El valor {valor} se repite {self.datos.count(valor)} veces.")

datos=[65, 78, 82, 90, 55, 67, 73, 89, 92, 76, 84, 61, 72, 85, 77, 80, 90, 63, 88, 82, 71, 75, 79, 91, 74, 68, 66, 83, 87, 93, 81, 69, 70, 88, 95, 58, 64, 89, 60, 73, 66, 76, 92, 84, 74, 67, 90, 85, 79, 83]
est=Estadistica(datos)
print(est.muestra())
print(est.frecuencias())