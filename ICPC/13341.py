# def sd(x):
#     return sum(int(d) for d in str(x))
# n = int(input().strip())
# nums = list(map(int, input().split()))
# nums.sort(key=lambda x: (sd(x), x))
# print(" ".join(map(str, nums)))
def suma_digitos(numero):
    return (sum(int(d) for d in str(numero)), len(str(numero)))

n = int(input())
v = [0]*n
v = list(map(int, input().split()))

numeros_ordenados = sorted(v, key=lambda numero: (suma_digitos(numero), numero))


for i in range(len(numeros_ordenados)-1):
    print(numeros_ordenados[i], end=" ")
    
print(numeros_ordenados[len(numeros_ordenados)-1])