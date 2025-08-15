#widget entry es para que el usuario pueda poner texto
from tkinter import *

raiz = Tk()

miframe= Frame(raiz,width=1200,height=600)
miframe.pack()

minombre=StringVar() # con eso se le dice que es una caden ade texto

def mostrar_nombre(event):
    # Si llamo get antes de que el usuario escriba, como si lo pongo seguido, 
    # entonces deja ""
    nombre = cuadroTexto.get()
    print(nombre)

cuadroTexto = Entry(miframe,)
cuadroTexto.grid(row=0,column=1)
cuadroTexto.config(fg="light pink",justify= "right")
# Bind ata eventos a funciones, solo a funciones 
cuadroTexto.bind("<Return>",mostrar_nombre)
nombre = cuadroTexto.get()
print(nombre)



cuadroTextoApellido = Entry(miframe,textvariable=minombre)
cuadroTextoApellido.grid(row=1,column=1)

cuadroTextoDireccion = Entry(miframe)
cuadroTextoDireccion.grid(row=2,column=1)

# ¿Cómo poner el texto como a la izquierda? hacemos un label 
# que también pertenezca al frame
#esa no es la forma más adecuada, con pack() es mejor, pero un nuevo método es grid
# que lo que hace es dividir en una cuadricula
nombreLabel=Label(miframe,text="Nombre:")
# sticky es para que aparezcan alineados, igual es con los puntos cardenales
nombreLabel.grid(row=0,column=0,sticky="w",padx=10,pady=10)

apellidoLabel=Label(miframe,text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky="w",padx=10,pady=10)

direccionLabel=Label(miframe,text="Direccion:")
direccionLabel.grid(row=2,column=0,sticky="w",padx=10,pady=10)
#padding, espacio entre el widget y el contenedor, en python
# padx:espacio para x
#pady: espacio paray

cuadropASS = Entry(miframe)
cuadropASS.grid(row=4,column=1)
cuadropASS.config(show="*")

label = Label(miframe,text="Contraseña: ")
label.grid(row=4,column=0, sticky="w",padx=10,pady=10)


comenlabel = Label(miframe,text="Comentarios: ")
comenlabel.grid(row=5,column=0, sticky="w",padx=10,pady=10)

textoComen = Text(miframe,width=50,height=10,padx=10,pady=100)
textoComen.grid(row=5,column=1)

#scrollbar que peretence al textoComen y es vertical por eso el y
scroll = Scrollbar(miframe,command=textoComen.yview)
#sticky="nsew") para que se adapte al tamaño y funcione el psoicionador
scroll.grid(row=5,column=2,sticky="nsew")
textoComen.config(yscrollcommand=scroll.set)

def codigoBoton():
    minombre.set("Juan")

butt= Button(miframe,text="enviar",padx=10,pady=10,command=codigoBoton)
butt.grid(row=6,column=1,pady=(20,0))

raiz.mainloop()