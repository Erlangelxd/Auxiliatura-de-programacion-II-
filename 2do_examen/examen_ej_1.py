class Estudiante:
    def __init__(self, edad, nota1, nota2, nota3):
        self.edad=edad
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
    def promedioCalificacion(self):
        promedio = (self.nota1+self.nota2+self.nota3)/3
        return promedio
class EstudiantePregrado(Estudiante):
    def __init__(self, edad, nota1, nota2, nota3):
        super().__init__(edad, nota1, nota2, nota3)
    def situacionEstudiante(self):
        if self.promedioCalificacion() >= 51:
            return f"Estudiante de pregrado aprobado"
        else:
            return f"Estudiante de pregrado reprobado"
class EstudiantePosgrado(Estudiante):
    def __init__(self, edad, nota1, nota2, nota3):
        super().__init__(edad, nota1, nota2, nota3)
    def situacionEstudiante(self):
        if self.promedioCalificacion() >= 71:
            return f"Estudiante de posgrado aprobado"
        else:
            return f"Estudiante de posgrado reprobado"
        

def main():
    iteraciones = int(input("N:"))
    for i in range(iteraciones):
        edad = int(input("Edad: "))
        nota1 = int(input("Nota 1:"))
        nota2 = int(input("Nota 2:"))
        nota3 = int(input("Nota 3:"))
        if edad >= 18 and edad <= 30:
            estudiante = EstudiantePregrado(edad, nota1, nota2, nota3)
            print(estudiante.situacionEstudiante())
        elif edad > 30:
            estudiante = EstudiantePosgrado(edad, nota1, nota2, nota3)
            print(estudiante.situacionEstudiante())
main()