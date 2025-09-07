class Personaje:
    def __init__(self, nombre, ki, raza, daño):
        self.nombre=nombre
        self.ki=ki
        self.raza=raza
        self.daño=daño
    def atacar(self, rival):
        rival.ki-=self.daño
        if rival.ki <= 0:
            rival.ki = 0
            return f"{rival.nombre} fué derrotado"
        return f"{self.nombre} ha atacado a {rival.nombre}, ahora tiene {rival.ki} de ki"
    def entrenar(self):
        self.ki*=2
        self.daño*=2
        return f"{self.nombre} ha entrenado y ahora tiene {self.ki} de ki y {self.daño} de daño"
    
class Sayayin(Personaje):
    def __init__(self, nombre, ki, raza, daño, cola, transformacion):
        super().__init__(nombre, ki, raza, daño)
        self.cola=cola
        self.transformacion=transformacion
    def kamehameha(self, rival):
        rival.ki-=self.daño*3
        if rival.ki <= 0:
            rival.ki = 0
            return f"Frezzer no te perdonare!!!!!!! {rival.nombre} fué derrotado"
        return f"{self.nombre} ha lanzado un Kamehameha a {rival.nombre}, ahora tiene {rival.ki} de ki"
    def calipjo(self, rival):
        rival.ki-=self.daño*3
        if rival.ki <= 0:
            rival.ki = 0
            return f"{rival.nombre} fué derrotado"
        return f"{self.nombre} ha lanzado un Calipjo a {rival.nombre}, ahora tiene {rival.ki} de ki"
    def transformarse(self):
        self.transformacion="Super Sayayin"
        self.ki*=20
        self.daño*=20
        return f"{self.nombre} se ha transformado en {self.transformacion}"

class Namekusei_jin(Personaje):
    def __init__(self, nombre, ki, raza, daño):
        super().__init__(nombre, ki, raza, daño)
    def regenerarse(self):
        self.ki-=10
        return f"{self.nombre} se ha regenerado, ahora tiene {self.ki} de ki"
    def makankosappo(self, rival):
        if rival.ki <= 0:
            rival.ki = 0
            return f"{rival.nombre} fué derrotado"
    def curar(self, aliado):
        aliado.ki+30
        return f"{self.nombre} ha curado a {aliado.nombre}, ahora tiene {aliado.ki} de ki"
    def curarse(self):
        self.ki+=30
        return f"{self.nombre} se ha curado, ahora tiene {self.ki} de ki"

class Changlong(Personaje):
    def __init__(self, nombre, ki, raza, daño):
        super().__init__(nombre, ki, raza, daño)
    def transformarse(self):
        self.ki*=20
        self.daño*=20
        return f"{self.nombre} se ha transformado"
    def atacar(self, rival):
        rival.ki-=self.daño
        if rival.ki <= 0:
            rival.ki = 0
            return f"{rival.nombre} explotó en mil pedazos"
        return f"{self.nombre} ha atacado a {rival.nombre}, ahora tiene {rival.ki} de ki"

goku=Sayayin("Goku", 100, "Sayayin", 50, False, "Base")
picoro=Namekusei_jin("Picoro", 80, "Namekusei-jin", 40)
krillin=Personaje("Krillin", 50, "Humano", 30)
frezzer=Changlong("Frezzer", 200, "Changlong", 70)
# print(picoro.atacar(frezzer))
# print(frezzer.atacar(picoro))
# print(picoro.curarse())
# print(frezzer.atacar(krillin))
# print(goku.transformarse())
# print(frezzer.transformarse())
# print(goku.kamehameha(frezzer))
# print(frezzer.atacar(goku))
# print(goku.kamehameha(frezzer))
