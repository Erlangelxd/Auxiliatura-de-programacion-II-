class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, otro): #sobrecarga del operador +
        return Vector(self.x + otro.x, self.y + otro.y)
    def __sub__(self, otro): #sobrecarga del operador -
        return Vector(self.x - otro.x, self.y - otro.y)
    def __mul__(self, otro): #sobrecarga del operador *
        return Vector(self.x * otro.x, self.y * otro.y)
    def __truediv__(self, otro): #sobrecarga del operador /
        return Vector(self.x / otro.x, self.y / otro.y)
    def __str__(self): #sobrecarga del metodo str para imprimir
        return f"({self.x}, {self.y})"
v1=Vector(2, 3)
v2=Vector(5, 6)
print(v1+v2)
print(v1-v2)    
print(v1*v2)
print(v1/v2)
