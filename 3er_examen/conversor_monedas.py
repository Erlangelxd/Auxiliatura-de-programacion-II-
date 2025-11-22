import tkinter as tk

app=tk.Tk()
app.title("Calculadora")
app.geometry("600x600")

dolar = 6.97
def calcular():
    valor = entrada.get()    
    boliviano = float(valor)*dolar
    etiqueta.config(text=str(boliviano) + " Bs")
def inflacion():
    dolar+=0.5
    print(dolar)
    
etiqueta=tk.Label(text="00.0") #Etiquetas
etiqueta.pack()
entrada=tk.Entry() #Entrada
entrada.pack()
boton=tk.Button(text="Calcular $ a Bs", command=calcular) #Boton
boton.pack()
app.mainloop()
