class OperacionBasica:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def suma(self):
        return self.x + self.y
    def resta(self):
        return self.x - self.y
    def multiplicacion(self):
        return self.x * self.y
    def divicion(self):
        try:
            division=self.x / self.y
            return division
        except ZeroDivisionError:
            return 0
 

# se necesita modelar una compañia con varios tipos de empleados.
# Empleados de tiempo completo, contratistas y gerentes. 
# Todos ellos tienen un nombre,id, pero sus salarios se calculan de manera 
# diferente.
# Los empleados de tiempo completo tienen un salario fijo, 
# los contratistas tienen un pago por hora 
# y los gerentes ganan un salario fijo mas un bono anual 


op1=OperacionBasica(10, 0)
print(op1.suma())
print(op1.resta())
print(op1.multiplicacion())
print(op1.divicion())
