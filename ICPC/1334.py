V=[]
sumas=[]
try:
    n=int(input("longiud: "))
    if 0 <= n and n <= 100:
        for i in range(n):
            m=n=int(input("valor: "))
            if 1 <= m and m <= 100000:
                V.append(m)
    print(V)
    for elemento in V:
        items=[]
        item=str(elemento)
        for i in range(len(item)):
            items.append(int(item[i]))
        sumas.append(sum(items))
    print(sumas.sort())

except ValueError:
    pass 
