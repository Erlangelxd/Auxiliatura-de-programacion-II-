class Personaje:
    def __init__(self, nombre, daño):
        self.nombre=nombre #atributos publicos
        self.__vida=100 #definimos el atributo Privado
        self.daño=daño
    def getVida(self): # GET retornar el valor de atributo privado
        return self.__vida
    def setVida(self, mod_vida): #SET para modificar el valor del atributo privado
        self.__vida=mod_vida
class Superviviente(Personaje):
    def __init__(self, nombre, daño):
        super().__init__(nombre, daño)
    def mostrar(self):
        return f"{self.nombre} - Vida: {self.vida}, Daño: {self.daño}"
    def atacar(self, infectado): #con encapsulasion
        infectado.setVida(infectado.getVida()-self.daño)
        if infectado.getVida() <= 0:
            infectado.setVida(0)
            return f"{infectado.nombre} ha sido derrotado"
        return f"{self.nombre} ha atacado a {infectado.nombre}, ahora tiene {infectado.vida} de vida"
# sin encapsulasion
    # def atacar(self, infectado): 
    #     infectado.vida=infectado.vida-self.daño
    #     if infectado.vida <= 0:
    #         infectado.vida = 0
    #         return f"{infectado.nombre} ha sido derrotado"
    #     return f"{self.nombre} ha atacado a {infectado.nombre}, ahora tiene {infectado.vida} de vida"
    def curarse(self): #con encapsulasion
        if self.getVida() < 100:
            self.setVida(self.getVida()+60)
            if self.getVida() > 100:
                self.setVida(100)
        elif self.getVida() >= 100:
            self.setVida(100)
            return f"{self.nombre} ya tiene la vida completa"
        return f"{self.nombre} se ha curado y ahora tiene {self.vida} de vida"
# sin encapsulasion
    # def curarse(self):
    #     if self.vida < 100:
    #         self.vida=self.vida+60
    #         if self.vida > 100:
    #             self.vida = 100
    #     elif self.vida >= 100:
    #         self.vida = 100
    #         return f"{self.nombre} ya tiene la vida completa"
    #     return f"{self.nombre} se ha curado y ahora tiene {self.vida} de vida"
    def curar(self, superviviente): #con encapsulasion
        if superviviente.getVida() < 100:
            superviviente.setVida(superviviente.getVida()+20)
        elif superviviente.getVida() >= 100:
            superviviente.setVida(100)
            return f"{superviviente.nombre} ya tiene la vida completa"
        return f"{self.nombre} ha curado a {superviviente.nombre}, ahora tiene {superviviente.vida} de vida"
    # def curar(self, superviviente):
    #     if superviviente.vida < 100:
    #         superviviente.vida=superviviente.vida+20
    #     elif superviviente.vida >= 100:
    #         superviviente.vida = 100
    #         return f"{superviviente.nombre} ya tiene la vida completa"
    #     return f"{self.nombre} ha curado a {superviviente.nombre}, ahora tiene {superviviente.vida} de vida"
    def revivir(self, superviviente): #con encapsulasion
        if superviviente.getVida() == 0:
            superviviente.setVida(50)
            return f"{self.nombre} ha revivido a {superviviente.nombre}, ahora tiene {superviviente.vida} de vida"
        return f"{superviviente.nombre} no necesita ser revivido"
    # def revivir(self, superviviente):
    #     if superviviente.vida == 0:
    #         superviviente.vida = 50
    #         return f"{self.nombre} ha revivido a {superviviente.nombre}, ahora tiene {superviviente.vida} de vida"
    #     return f"{superviviente.nombre} no necesita ser revivido"
class Infectado(Personaje):
    def __init__(self, nombre, vida, daño):
        super().__init__(nombre, vida, daño)
    def atacar(self, superviviente):
        superviviente.vida=superviviente.vida-self.daño
        if superviviente.vida <= 0:
            superviviente.vida = 0
            return f"{superviviente.nombre} ha sido derrotado"
        return f"{self.nombre} ha atacado a {superviviente.nombre}, ahora tiene {superviviente.vida} de vida"
    
superviviente1=Superviviente("Ellis", 30)
superviviente2=Superviviente("Nick", 20)
print(superviviente1.nombre)
print(superviviente1.getVida()) 
# infectado1=Infectado("Boomer", 20)
# infectado2=Infectado("Tank", 50)

#PARTICIPACION
# Modificar la clase infectado para que trabaje con la encapsulacion
# Con el infectado Tank matar a Nick y que Ellis lo reviva
