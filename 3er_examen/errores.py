codigo = "for i in range(5 print(i)"  # Código inválido

try:
    exec(codigo)
except SyntaxError as e:
    print("SyntaxError detectado:", e)


try:
    print(variable_que_no_existe)
except NameError as e:
    print("NameError detectado:", e)


try:
    lista = [10, 20, 30]
    print(lista[5])
except IndexError as e:
    print("IndexError detectado:", e)


try:
    resultado = "10" + 5
except TypeError as e:
    print("TypeError detectado:", e)



try:
    numero = int("abc")
except ValueError as e:
    print("ValueError detectado:", e)
