linea=input().split()
N=int(linea[0])
C=int(linea[1])
palabras=[]
for i in range(N):
    palabras.append(input().strip())

print(palabras)
dict={}
for palabra in palabras:
    posicion=-1
    for i in range(C):
        if palabra[i]=="*":
            posicion=i
            break

    for letra in "abcdefghijklmnopqrstuvwxyz":
        posible=palabra[:posicion]+letra+palabra[posicion+1:]
        if posible not in dict:
            dict[posible]=0
        dict[posible]+=1
    print(dict)

for posible, contador in dict.items():
    print(posible, contador)
    if contador > -1 
# contador_xd=-1
# palabra_xd=None
# for posible, contador in dict.items():
#     if contador > contador_xd or (contador == contador_xd and posible < palabra_xd):
#         a=contador
#         b=posible

# print(b, a)