from tkinter import *
from tkinter import ttk

root = Tk()
root.title("IMC CALCULATOR")
def calculate(*args):
    try:
        valor1 = float(altura.get())
        valor2 = float(peso.get())   
        valor3 = (valor2 / (valor1 * valor1))
        resultado = round(valor3, 2)
        imc.set(f"IMC = {resultado}")
    except ValueError:
        pass
    

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

altura = StringVar()
altura_entry = ttk.Entry(mainframe , width=10, textvariable=altura)
altura_entry.grid(column=1, row=2, sticky=(W, E))
altura.set("ALTURA")

peso = StringVar()
peso_entry = ttk.Entry(mainframe, width=10, textvariable=peso)
peso_entry.grid(column=1, row=3, sticky=(W,E))
peso.set("PESO")


imc = StringVar()
ttk.Label(mainframe , textvariable=imc).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe , text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)
imc.set('IMC = ')

ttk.Label(mainframe, text= "Calculadora De IMC").grid(column = 2, row=1) 

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
