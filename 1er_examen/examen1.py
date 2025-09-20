class NumeroEspecial:
    def __init__(self, x):
        self.x=x
    def capicua(self):
        cap=str(self.x)
        if cap[::-1] == str(self.x):
            return 1
        else:
            return 0
    def es_primo(self):
        c=0
        for i in range(2,self.x):
            if (self.x % i == 0):
                c=c+1
        if c==0:
            return 1
        else:
            return 0

def main():
    x= int(input("x: "))
    if x>100:
        y=int(input("y: "))
        if (y>x):
            for i in range(x,y+1):
                num= NumeroEspecial(i)
                if (num.capicua() == 1):
                    print(f"Capicua {i}")
                if num.es_primo() == 1:
                    print(f"Primo {i}")
        else:
            print("Yno es mayor a x")
    else:
        print("X no es mayor a 100")
main()




