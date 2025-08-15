from tkinter import *

# La raíz es como la ventana principal, sobre la que no va construyendo
raiz = Tk()
raiz.title("Mi primera ventana en python")

# para evitar que se pueda cambiar el tamaño, acepta parametros bool, el primero es el ancho y el alto

#raiz.resizable(True,0)

# Se puede cambiar el iconoc, que no sea la pluma, se ocupa tener algo .ico

raiz.iconbitmap("rataOjona.ico")

#también podemos cambiar el tamaño por defecto

#raiz.geometry("650x350")

# con el metodo config se pueden hacer varias cosas, pero pro ejemplo se puede cambiar el color

raiz.config(bg="light pink")


# Un frame es como el contenedor

miFrame = Frame()

# No basta solo con crear el Frame hay que enpaquetarlo, o sea meterlo a la raíz, es como que este en ningun lugar

# En el método del empaquetado también es en elq ue podemos cambiar como aparece el frame, o sea en que posición 
#anchor es para los puntos cardenales, así podemos ponerlo con varias opciones???
#miFrame.pack(side="bottom", anchor="n")  # esto directamente no cambia nada
#Para que lo rellene
miFrame.pack(fill= "both", expand="True")  # Con esto se va expandiendo a lo horizontal, con y, no lo hace vertical, hay que usar un expand true, para ambos usamos both
#miFrame.pack(fill= "both")
#para verlo hay que darle color de fondo
#Para cambiar tamaño hay que quitar el geometry de la ventana, un frame tiene tamaño fijo, a diferencia de la ventana que se mueve como quiera
miFrame.config (bg = "light blue" , width="650 ", height="350" )  # Aun con esto solo no aparece, porque falta darle tamaño
#También se le puede cambair por ejemplos los bordes, antes hay que decirle que nos de un borde con un grosor distinto al que viene por defecto que es 0
miFrame.config(bd="35")
miFrame.config(relief= "groove")

#podemos incluso cambiar el cursos que cuando se pone en el frame
miFrame.config(cursor="pirate")
# Para que pueda funcionar debe de estar como en un bucle infinito
# Es muy importante que el main loop este siempre al final


#Todo lo del frame se le puede aplicar  a la raíz igual 

#==== Labels: nos permite poner texto, no se interactura, es una clase, se crea 
# una variable, se crea un objeto de tipo label y se la manda en el constructor 
# el contenedor donde va a estar el label, y las opciones, hay muchas, hay que
# la documentación


raiz.mainloop()

