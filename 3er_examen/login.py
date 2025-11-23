import tkinter as tk

app = tk.Tk()
app.title("Login")
app.geometry("500x500")

usuario = "Erlan"
contraseña = "12345"

def login():
  us = entrada1.get()
  cn = entrada2.get()
  if us == usuario and cn == contraseña:
    respuesta.config(text="Login exitoso")
  else:
    respuesta.config(text="Login fallido")

h1 = tk.Label(text="Login", font=("Arial", 20))  
h1.pack()
texto1= tk.Label(text="Ingresa tu usuario: ", font=("Arial", 20))
texto1.pack()
entrada1 = tk.Entry(font=("Arial", 20))
entrada1.pack()
texto2= tk.Label(text="Ingresa tu contraseña: ", font=("Arial", 20))
texto2.pack()
entrada2 = tk.Entry(font=("Arial", 20))
entrada2.pack()
boton = tk.Button(text="Ingresar", font=("Arial", 20), command=login)
boton.pack()
respuesta = tk.Label(text="......", font=("Arial", 20))
respuesta.pack()
app.mainloop()