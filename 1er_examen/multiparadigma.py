import math
print(math.factorial(5))

x=int(input("n1: "))
y=int(input("n2: "))
suma=x+y
print(suma)

def suma(x, y):
    return x+y
suma(2,3)

class Suma():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def solucion(self):
        return self.x + self.y

obj=Suma(2, 2)
obj.solucion() 