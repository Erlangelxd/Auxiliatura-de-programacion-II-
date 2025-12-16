from tkinter import *

app = Tk()

app.title("Calculadora")

def insertar(valor):
  pantalla.insert(END, valor)

def borrar():
  pantalla.delete(0, END)

def operacion():
  resultado = pantalla.get()
  resultado = eval(resultado)
  pantalla.delete(0, END)
  pantalla.insert(0, resultado)

pantalla = Entry(app, font=("Arial 20"))
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

boton1 = Button(app, text="1", width=5, height=2, command=lambda: insertar(1))
boton2 = Button(app, text="2", width=5, height=2, command=lambda: insertar(2))
boton3 = Button(app, text="3", width=5, height=2, command=lambda: insertar(3))
boton4 = Button(app, text="4", width=5, height=2, command=lambda: insertar(4))
boton5 = Button(app, text="5", width=5, height=2, command=lambda: insertar(5))
boton6 = Button(app, text="6", width=5, height=2, command=lambda: insertar(6))
boton7 = Button(app, text="7", width=5, height=2, command=lambda: insertar(7))
boton8 = Button(app, text="8", width=5, height=2, command=lambda: insertar(8))  
boton9 = Button(app, text="9", width=5, height=2, command=lambda: insertar(9))
boton0 = Button(app, text="0", width=5, height=2, command=lambda: insertar(0))

boton_multiplicar = Button(app, text="x", width=5, height=2, command=lambda: insertar("*"))
boton_dividir = Button(app, text="/", width=5, height=2, command=lambda: insertar("/"))
boton_sumar = Button(app, text="+", width=5, height=2, command=lambda: insertar("+"))
boton_restar = Button(app, text="-", width=5, height=2, command=lambda: insertar("-"))

boton_igual = Button(app, text="=", width=5, height=2, command=operacion)
boton_borrar = Button(app, text="C", width=5, height=2, command=borrar)

boton7.grid(row=1, column=0, padx=5, pady=5)
boton8.grid(row=1, column=1, padx=5, pady=5)
boton9.grid(row=1, column=2, padx=5, pady=5)
boton_dividir.grid(row=1, column=3, padx=5, pady=5)
boton4.grid(row=2, column=0, padx=5, pady=5)
boton5.grid(row=2, column=1, padx=5, pady=5)
boton6.grid(row=2, column=2, padx=5, pady=5)
boton_multiplicar.grid(row=2, column=3, padx=5, pady=5)
boton1.grid(row=3, column=0, padx=5, pady=5)
boton2.grid(row=3, column=1, padx=5, pady=5)
boton3.grid(row=3, column=2, padx=5, pady=5)
boton_restar.grid(row=3, column=3, padx=5, pady=5)
boton0.grid(row=4, column=0, padx=5, pady=5)
boton_borrar.grid(row=4, column=1, padx=5, pady=5)
boton_igual.grid(row=4, column=2, padx=5, pady=5)
boton_sumar.grid(row=4, column=3, padx=5, pady=5)

#Agregar los boton de "(", ")", "**(1/2) <= raiz cuadrada, "**" <= potencia

app.mainloop()
