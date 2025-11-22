import tkinter as tk

app=tk.Tk()
app.title("Calculadora")
app.geometry("500x500")

def operar():
    valor1=a.get()
    operacion = eval(valor1)
    resultado.config(text=operacion)
resultado=tk.Label(text=".......")
resultado.pack()
a=tk.Entry()
a.pack()
boton=tk.Button(text="Calcular", command=operar)
boton.pack()
app.mainloop()