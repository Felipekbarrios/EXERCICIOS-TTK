from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Senha aleatoria")

def gerar_senha():
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Numeros = '0123456789'
    especial = '@!#&*()_<+-={[}]:;''">,.?/'
    senha = []
    all = [caracteres,Numeros,especial]
    for i in range(8):
        a = random.choice(all)
        b = random.choice(a)
        senha.append(b)
    senha2 = ''.join(senha)
    resultado.set(senha2)
    

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


resultado = StringVar()
ttk.Label(mainframe , textvariable=resultado).grid(column=2, row=1, sticky=(W, E))
ttk.Button(mainframe , text="Gerar", command=gerar_senha).grid(column=2, row=3, sticky=W)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
