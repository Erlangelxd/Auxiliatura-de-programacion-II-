

def area(*args):
    print(len(args))
    if len(args)==1:
        radio = args[0]
        area = 3.1416 * radio ** 2
        print(f"{area} del circulo")
    elif len(args) == 2:
        base = args[0]
        altura = args[1]
        area = (base * altura)/2
        print(f"{area} del triangulo")

area(6)