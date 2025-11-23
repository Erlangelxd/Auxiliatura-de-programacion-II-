import tkinter as tk

app = tk.Tk()
app.title("Conversor de temperatura")
app.geometry("500x500")

def convertir():
  temperatura = entrada.get()
  farenheit = (int(temperatura) * 9/5) + 32
  mostrar.config(text=str(farenheit) + "ºF")

mostrar = tk.Label(text="..........", font=("Arial", 20))
mostrar.pack()
entrada = tk.Entry(font=("Arial", 20))
entrada.pack()
boton = tk.Button(text="Convertir", font=("Arial", 20), command=convertir)
boton.pack()


app.mainloop()


