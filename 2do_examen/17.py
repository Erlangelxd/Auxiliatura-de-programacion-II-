class Empleado:
    def __init__(self, nombres, sueldo_base):
        self.nombres=nombres
        self.sueldo_base=sueldo_base
    def calcularSueldo(self, horas):
        self.sueldo_base += 20*horas
        return (f"Sueldo a pagar: {self.sueldo_base}")
    
class Administrativo(Empleado):
    def __init__(self, nombres, sueldo_base, horas_extra, bonificacion):
        super().__init__(nombres, sueldo_base)
        self.horas_extra=horas_extra
        self.bonificacion=bonificacion
    def calcularSueldo(self):
        self.sueldo_base += 20*self.horas_extra + self.bonificacion 
        return (f"Sueldo a pagar: {self.sueldo_base}")
    
class Operarios(Empleado):
    def __init__(self, nombres, sueldo_base, horas_extra, tarifa_horas_extra):
        super().__init__(nombres, sueldo_base)
        self.horas_extra=horas_extra
        self.tarifa_horas_extra=tarifa_horas_extra
    def calcularSueldo(self):
        self.sueldo_base += self.tarifa_horas_extra*self.horas_extra   
        return (f"Sueldo a pagar: {self.sueldo_base}")
empl1=Empleado("Juan", 1000)
print(empl1.calcularSueldo(5))
empl2=Administrativo("Maria", 3500, 10, 200)
print(empl2.calcularSueldo())
empl3=Operarios("Carlos", 2000, 5, 30)
print(empl3.calcularSueldo())