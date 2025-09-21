class NumeroEspecial:
    def __init__(self, x):
        self.x=x
    def capicua(self):
        comparar=str(self.x)[::-1]
        if comparar == str(self.x):
            return f"Es Capicua"
        else:
            return f"No es Capicua"
    def primos(self):
        c=0
        for i in range(2, self.x):
            if self.x % i == 0:
                c+=1
        if c == 0:
            return 1
        else:
            return 0

def main():
    x=int(input("x: "))
    if x>100:
        y=int(input("y: "))
        if y>x:
            for i in range(x, y+1):
                numero=NumeroEspecial(i)
                if numero.capicua() == "Es Capicua":
                    print("Es Capicua", i)
                if numero.primos() == 1:
                    print("Es primo", i)
        else:
            print("y debe ser mayor que x")
    else:
        print("x debe ser mayor que 100")

main()