N=int(input())
cadena=input()
cantidad=[]
for i in range (len(cadena)):
    for j in range(len(cadena)):
        if cadena[i] == cadena[j]:
            cantidad.append(cadena[i])
            cantidad.append(cadena[j])

print(cantidad)


    