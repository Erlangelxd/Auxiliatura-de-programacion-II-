import tkinter as tk
from tkinter import messagebox

class VerificarEdad():
  def __init__(self, raiz):
    self.raiz = raiz
    self.raiz.title("Verificar edad")
    self.raiz.geometry("500x500")
    self.crear_componentes()
  def crear_componentes(self):
    self.texto = tk.Label(self.raiz, text="Ingresa tu edad: ", font=("Arial", 20))
    self.texto.pack()
    self.entrada = tk.Entry(self.raiz, font=("Arial", 20))
    self.entrada.pack()
    self.boton = tk.Button(self.raiz, text="Verificar", font=("Arial", 20), command=self.verificar)
    self.boton.pack()
  def verificar(self):
    edad = self.entrada.get()
    if int(edad) >= 18:
      messagebox.showinfo("Eres mayor de edad")
    else:
      messagebox.showerror("Eres menor de edad")

raiz = tk.Tk()
app = VerificarEdad(raiz)
raiz.mainloop()