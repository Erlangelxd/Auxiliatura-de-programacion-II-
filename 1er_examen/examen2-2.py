class OperacionBasica:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def suma(self):
        return self.x + self.y 
    def resta(self):
        return self.x - self.y
    def multiplica(self):
        return self.x * self.y
    def dividir(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
            return 0

def main():
    N = int(input("N de iteraciones:"))
    for i in range(1, N+1):
        x=int(input("x:"))
        y=int(input("y:"))
        operaciones=OperacionBasica(x, y)
        print("La suma es: ", operaciones.suma())
        print("La resta es: ",operaciones.resta())
        print("El producto es: ",operaciones.multiplica())
        print("La division es: ",operaciones.dividir())

main()