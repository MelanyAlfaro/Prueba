from tkinter import * 
root = Tk()
# primer parm le dice queine es el padre, donde vive
miFrame = Frame(root, width=500 , height=400)
# con pack se le dice  a tinder que lo dibuje y donde colorle 
# dentro de root, pack lo coloca directamenbte, pero se puede 
# por ejemplo con .grid color en una ciadríacula o con .place colocaro 
# con coordenadas exactas
miFrame.pack()
#así solo, al empaquetar el texto en el frame, entonces el frame se adapta a las dimensiones del texto
# para que se quede el tamaño del frame, y además darle posición al label, se usa un método distinto
miLabel = Label(miFrame, text= "Esto es una pruebita <3")#miLabel = Label(miFrame, text= "Esto es una pruebita <3")
#miLabel.pack()
miLabel.place(x=100,y=200)

#Se puede hacer lo mismo pero sin crear un variable
Label(miFrame,text = "Holaaa  :3", fg = "red", font=("Times New Roman", 12)).place(x=100,y=150)

#también se puede poner imagenes
miImg = PhotoImage(file="rataOjona.png")

Label(miFrame,image=miImg).place(x=300,y=100)


root.mainloop()