class Persona:
    def __init__(self, nombre, edad, genero, **kwargs):
        self.nombre = str(nombre)
        self.edad = int(edad)
        self.genero = genero
        super().__init__(**kwargs)
    def comer(self):
        return f"{self.nombre} está comiendo"
    def saludar(self):
        return f"{self.nombre} está saludando"

class Ingeniero(Persona):
    def __init__(self, especialidad_ingenieria, **kwargs):
        self.especialidad_ingenieria = especialidad_ingenieria
        super().__init__(**kwargs)
    def calcular_conversiones(self, numero):
        resultado = bin(numero)
        return f"{self.nombre} ha convertido el número {numero} a binario: {resultado}"

class Medico(Persona):
    def __init__(self, especialidad_medica, hospital, **kwargs):
        self.especialidad_medica = especialidad_medica
        self.hospital = hospital
        super().__init__(**kwargs)
    def diagnosticar(self, paciente):
        return f"El médico {self.nombre} está diagnosticando al paciente {paciente} en el hospital {self.hospital}"
    def ubicacion(self):
        return f"El médico {self.nombre} trabaja en el hospital {self.hospital}"

class IngenieroBiomedico(Ingeniero, Medico):
    def __init__(self, nombre, edad, genero, especialidad_ingenieria, especialidad_medica, hospital, años_de_experiencia):
        self.años_de_experiencia = años_de_experiencia
        super().__init__(
            nombre=nombre,
            edad=edad,
            genero=genero,
            especialidad_ingenieria=especialidad_ingenieria,
            especialidad_medica=especialidad_medica,
            hospital=hospital
        )
    def reparar_equipo(self, equipo):
        return f"El ingeniero biomédico {self.nombre} está reparando el equipo {equipo} en el hospital {self.hospital}"

ing1 = Ingeniero(especialidad_ingenieria="Testing", nombre="Jose", edad=20, genero="Masculino")
ing2 = Ingeniero(especialidad_ingenieria="DevOps", nombre="Maria", edad=20, genero="Femenino")
print(ing2.calcular_conversiones(2))
medico1 = Medico(especialidad_medica="Pediatria", hospital="Hospital del norte", nombre="Ana", edad=30, genero="Femenino")
print(medico1.diagnosticar("Pedro"))
print(medico1.ubicacion())
ingbio = IngenieroBiomedico("Luis", 40, "Masculino", "Mecanica", "Cardiologia", "Hospital del norte", 10)
print(ingbio.reparar_equipo("Resonancia Magnetica"))