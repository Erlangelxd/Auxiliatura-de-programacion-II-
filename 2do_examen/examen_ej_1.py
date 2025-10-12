class Figura:
    def calcular_area(self, *args):
        if len(args) == 2:
            base = args[0]
            altura = args[1]
            area = base * altura
            print(f"El area del rectangulo es {area}")
        elif len(args) == 1:
            radio = args[0]
            area = 3.1416 * radio**2
            print(f"El area del circulo es {area}")
        else:
            print("Error")

#agregar la funcionalidad de recibir 3 argumentos 
#y calcular el area de un trapecio
# en caso de que se reciban mas de 3 elementos lanzar un mensaje de error


fig=Figura()
fig.calcular_area(10, 25)
fig.calcular_area(2)
