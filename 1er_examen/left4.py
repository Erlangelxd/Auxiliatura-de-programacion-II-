class Personaje:
    def __init__(self, nombre, vida, daño):
        self.nombre=nombre
        self.vida=vida
        self.daño=daño
class Superviviente(Personaje):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)
    def atacar(self, infectado):
        infectado.vida=infectado.vida-self.daño
        if infectado.vida <= 0:
            infectado.vida = 0
            return f"{infectado.nombre} ha sido derrotado"
        return f"{self.nombre} ha atacado a {infectado.nombre}, ahora tiene {infectado.vida} de vida"
    def curarse(self):
        if self.vida < 100:
            self.vida=self.vida+30
        elif self.vida >= 100:
            self.vida = 100
            return f"{self.nombre} ya tiene la vida completa"
        return f"{self.nombre} se ha curado y ahora tiene {self.vida} de vida"
    def curar(self, superviviente):
        if superviviente.vida < 100:
            superviviente.vida=superviviente.vida+20
        elif superviviente.vida >= 100:
            superviviente.vida = 100
            return f"{superviviente.nombre} ya tiene la vida completa"
        return f"{self.nombre} ha curado a {superviviente.nombre}, ahora tiene {superviviente.vida} de vida"
    def revivir(self, superviviente):
        if superviviente.vida == 0:
            superviviente.vida = 50
            return f"{self.nombre} ha revivido a {superviviente.nombre}, ahora tiene {superviviente.vida} de vida"
        return f"{superviviente.nombre} no necesita ser revivido"
class Infectado(Personaje):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)
    def atacar(self, superviviente):
        superviviente.vida=superviviente.vida-self.daño
        if superviviente.vida <= 0:
            superviviente.vida = 0
            return f"{superviviente.nombre} ha sido derrotado"
        return f"{self.nombre} ha atacado a {superviviente.nombre}, ahora tiene {superviviente.vida} de vida"
    
superviviente1=Superviviente("Ellis", 50, 30)
superviviente2=Superviviente("Nick", 100, 20)
infectado1=Infectado("Boomer", 30, 20)
infectado2=Infectado("Tank", 1000, 50)
print(infectado2.atacar(superviviente2))
print(infectado2.atacar(superviviente2))

print(superviviente1.revivir(superviviente2))
print(superviviente2.curarse())
print(superviviente1.atacar(infectado1))