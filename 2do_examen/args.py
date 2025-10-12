def sumar(x, y):
    return x+y

print(sumar(2, 5))


def suma2(*args):  # *args para recibir N elementos
    print(sum(args))

print(suma2(1, 2, 3, 4, 5, 6, 7, 8, 9)) 


# [1,2,3,4,5,6,7,12,9] # array   MUTABLE
# {
#     "clave" : valor   # diccionarios MUTABLE
# } 

# (1,2,3,4,5) # tuplas IMNUTABLE