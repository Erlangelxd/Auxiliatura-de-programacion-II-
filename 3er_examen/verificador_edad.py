import tkinter as tk

app=tk.Tk()
app.title("Calculadora de edad")
app.geometry("500x500")

def calcular():
    edad = entrada.get()
    if int(edad) >= 18:
        resultado.config(text="Eres mayor de edad")
    else:
        resultado.config(text="Eres menor de edad")
        
enunciado = tk.Label(text="Dame tu edad")
enunciado.pack()
entrada = tk.Entry()
entrada.pack()
boton = tk.Button(text="Calcular", command=calcular)
boton.pack()
resultado= tk.Label(text=" ")
resultado.pack()
app.mainloop()
