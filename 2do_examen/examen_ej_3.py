class Estudiante:
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        self.nombre=nombre
        self.edad=edad
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
    def promedioCalificacion(self):
        promedio = (self.nota1 + self.nota2 +  self.nota3)/3
        return promedio
    
class EstudiantePregrado(Estudiante):
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        super().__init__(nombre, edad, nota1, nota2, nota3)
    def situacionEstudiante(self):
        if self.promedioCalificacion() >= 51:
            return f"Estudiante de pregrado aprobado"
        else:
            return f"Estudiante de pregrado reprobado"
class EstudiantePostgrado(Estudiante):
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        super().__init__(nombre, edad, nota1, nota2, nota3)
    def situacionEstudiante(self):
        if self.promedioCalificacion() >= 71:
            return f"Estudiante de postgrado aprobado"
        else:
            return f"Estudiante de postgrado reprobado"

def main():
    N = int(input("N: "))
    for i in range(N):
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        nota1 = int(input("Nota 1: "))
        nota2 = int(input("Nota 2: "))
        nota3 = int(input("Nota 3: "))
        if edad >= 18 and edad <= 30:
            est = EstudiantePregrado(nombre, edad, nota1, nota2, nota3)
            print(est.situacionEstudiante())
        elif edad > 30:
            est = EstudiantePostgrado(nombre, edad, nota1, nota2, nota3)
            print(est.situacionEstudiante())
        

    
main()