from io import open

# archivo_texto = open ("archivo.txt","w")
# archivo_texto.write("This es waier easier than in C \n martina \n patos \n  odio a los furros")
# archivo_texto.close()

# #para abrir en lectura

# archivo_texto=open("archivo.txt", "r")
# texto = archivo_texto.read()
# archivo_texto.close()
# print(texto)

# #readlines lee linea por línea y lo guarda en unarray
# archivo_texto=open("archivo.txt", "r")
# lineas_texto = archivo_texto.readlines()
# archivo_texto.close()

# print(lineas_texto)
# print(len(lineas_texto))
# print(lineas_texto[2])

# for i in range (len(lineas_texto)):
#     print(lineas_texto[i])

# #Para agregar sin sobreescibir se le pone a de append

# archivo_texto = open ("archivo.txt" , "a")

# archivo_texto.write("\n siempre he amado al osito")

# archivo_texto.close()


#========================================
# Cambiar posición del cursor. Al hacer un read niral siempre inicia al inicio y se queda, si hago la instrucción dos veces no habría nada


archivo_texto = open("archivo.txt","r")

print(archivo_texto.read())

print("---Puntero desde la posición 10")

archivo_texto.seek(10)

print(archivo_texto.read())

#read también lo puede hacer, solo que hace la lectura hasta una posición que uno le diga
archivo_texto.seek(0)

print("---Puntero hasta la posición 10")
print(archivo_texto.read(10))

archivo_texto.seek(0)

print("---Puntero hasta la posición 10")
print(archivo_texto.readline())

archivo_texto.close()

#También se puede abrir para leer y escribir
 
archivo_texto = open("archivo.txt" , "r+")

archivo_texto.write("Comienzo del texto")
