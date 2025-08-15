from tkinter import *

root= Tk()

MenuWindow = None 
opcionC = None

def anterior():
    global MenuWindow
    global opcionC
    MenuWindow.deiconify()
    opcionC.destroy()

def openC():
    global MenuWindow
    global opcionC
    MenuWindow.withdraw()
    print("abrir nueva ventana")
    opcionC = Toplevel (MenuWindow)
    anteriorButt = Button(opcionC,text="Anterior",command=lambda:anterior())
    anteriorButt.pack()

def openMenu():
    global MenuWindow 
    print("abrir nueva ventana")
    MenuWindow = Toplevel(root)
    yosButton=Button(MenuWindow, text="opción c",command=lambda:openC())
    yosButton.pack()

    
    

MenuButtom = Button(root,text="ir a menu", command=lambda:openMenu())
MenuButtom.pack()



root.mainloop()