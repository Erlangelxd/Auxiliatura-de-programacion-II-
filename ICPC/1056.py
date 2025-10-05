import sys

def main():
    n = int(sys.stdin.readline().strip())
    
    for i in range(n):
        a = sys.stdin.readline().strip()
        numeros = sys.stdin.readline().split()
        
        resultado = ' '.join(numeros[::-1]) + '\n'
        sys.stdout.write(resultado)

if __name__ == "__main__":
    main()