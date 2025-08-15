from tkinter import *
# este no fnciona
root = Tk()

varOpción= IntVar()
def imprimir():
    print(varOpción.get())

    if varOpción.get ==1 :
        etiqueta.config (text = "has elegido masculino")

Label (root, text= "Género:").pack()

Radiobutton(root, text="Masculino", variable= varOpción, value=1, command= imprimir).pack()

Radiobutton(root,text="Femenino",variable= varOpción, value=1).pack()

etiqueta = Label (root)
etiqueta.pack()




root.mainloop()