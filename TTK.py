from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")
def calculate(*args):
    try:
        valor = float(milhas.get())  
        km.set(valor * 1.609344)     
    except ValueError:
        pass
    

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

milhas = StringVar()
feet_entry = ttk.Entry(mainframe , width=7, textvariable=milhas)
feet_entry.grid(column=2, row=1, sticky=(W, E))

km = StringVar()
ttk.Label(mainframe , textvariable=km).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe , text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe , text="Milha").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe , text="É Equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe , text="Km").grid(column=3, row=2, sticky=W)


root.mainloop()