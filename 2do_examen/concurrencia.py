import threading

lock = threading.Lock()

def escribir(nombre):
    with lock:
        with open("estudiantes.txt", "a") as archivo:
            archivo.write(nombre + "\n")

h1 = threading.Thread(target=escribir, args=("Erlan",)) 
h2 = threading.Thread(target=escribir, args=("Angel",))
h1.start()
h2.start()
h2.join()
h2.join()
print("Escritura completada.")