# mensaje = "Tragic, no hay main"
# print(mensaje)
# print("Puedo solo imprimir así")
# a=2
# print (a**2)
# for i in range(5):
#     a+=1
#     print(a)
# print ("Parece que sí cambia lo que está dentro de un bloquse")
# print (a**2)
# print(type(a))

# numero1=5
# numero2=7 
# if numero1 >= numero2:
#     print("el número", numero1, "es mayor que el número " ,numero2)
# else:
#     print("el número", numero2, "es mayor que el número " ,numero1)

# numPrueba = 5
# while numPrueba >= 2 :
#     print(numPrueba)
#     numPrueba-=1


# def suma(num1,num2):
#     print("llamada a la función")
#     print("la suma es: ", num1+num2)



# def mult(num1,num2):
#     return num1*num2

# print("Como no hay tipos, funciona como un template, o sea se le puede pasar cualquier cosa")
# suma(1,2)
# suma(-1,2)
# suma(2.0,5.5)

# print(mult(2,2))
# print(mult(-10,2))

# def changeNum(num):
#     print("llamada a función")
#     num =5 

# numPrueba2 = 10
# print(numPrueba2)
# changeNum(10)
# print(numPrueba2)

# # Lista=array, en python pueden guardar diferentes tipos de valores
# # y se puede expandir dinámicamente nuevos elementos

# miArr = ["pato",1,2,4]

# for i in range (4) :
#     print(miArr[i])

# print ("Cuando poemos un indice negativo accede como a la inversa")

# print("indice -1: " ,miArr[-1])
# print("indice -1: " ,miArr[-2])

# print ("Con solo usar la palabra print se imprime todo el arreglo y \
# con #:# se imprime un range del arreglo, exclusive, no toma el ultimo valor. \
# Y se puede omitir el cero y lo toma como cero")

# print(miArr)
# print(miArr[0:2])
# print(miArr[:3])
# print("Incluso se puede acceder solo a los ultimos elementos, si uno pone solo un numero antes de :")
# print(miArr[2:])

# print("Para agregar cosas utilizamos .append, lo agrega al final")

# print("original:" , miArr)
# miArr.append("dog")
# print("luego de append: ", miArr)

# print("También con insert se le puede agregar elementos en un lugar especifico, nos pide como argumento el indice que queremos")

# print("original:" , miArr)
# miArr.insert(1,"mapache")
# print("luego de insert: ", miArr)
# print("original:" , miArr)
# miArr.insert(10,"esternoclenomastoideo")
# print("luego de insert en un indice que no existe: ", miArr)

# miArr.insert(-2,10.5)
# print("luego de insert en un indice que no existe: ", miArr)

# print("Con extend también podemos agregarle varios elementos, al final")
# miArr.extend(["zapato",-11,88])
# print(miArr)

# print("Con index podemos obtener el índice de un elemento especifico")
# print("indice de dog", miArr.index("dog"))

# #Cuando hay elementso repetidos me devuleve el primero que se encuentre
# # También podemos saber si un elemento se encyentra o no en un arreglo
# print("¿Está el elemento dog en la lista?: " , "dog" in miArr)
# print("¿Está el elemento 133 en la lista?: " , 133 in miArr)

# print ( "para eliminar usamos remove y el elemento tal cual")
# print(miArr)
# miArr.remove("dog")
# print(miArr)
# print (" También podemos eleiminar el ultimo elemento con pop")
# miArr.pop()
# print(miArr)

# # Hay operador para sumar listas

# print("Se puede usar + para juntar listas")

# miArr2 = ["puerco"]

# miLista = miArr + miArr2

# print(miLista)

# print("Se puede usar * para que se multiplique el contendio de la lista en el mismo array")
# print (miArr*3)

# #=======Tuplas============

# # Son como listas, pero inmutables, no se puede cambiar, no se puede añadir, eliminar, mover, etc. 
# # no se pueden usar varios de las funciones de los aray. Si permiten extraer porciones, 
# # y comprobar si un elemento esta. Ocupa menos espacio en memoria
# # es más rápido en ejecución. La sintaxis es igual, solo que en () en lugar de []

# print("")
# print("Ejemplos de tupla")
# # se puede como tupla = 1,2,3 pero es mejor con ()
# tupla = 1,2,3
# print (tupla)
# print (tupla[1])
# print("Podemso convertir tuplas a array, y array a tuplas con list")
# miLista = list(tupla)
# print(miLista)
# print("Podemso convertir tuplas a array, y array a tuplas con list")
# miTupla = tuple(miLista)
# print(miTupla)
# print ("podemso saber si un elemento está en una tupla con in")
# print (3 in miTupla)
# print ("podemos saber cuantas veces hay un elemento en una lista con .count (elemento)")
# print (miTupla.count(3))
# print("También podemos ver que tan larga es una tupa")
# print(len(miTupla))
# print("Se puede crear una tabla y bariables, y al igualar las variables a la tupla, se le asignan los valore")
# nueva = ("Joshua", 21, "Culon")
# nombre,edad,caracteristica = nueva

# print(nombre)
# print(edad)
# print(caracteristica)

# #===== diccionarios===========

# # Cada valor tiene una clave unica, se puede almacenar cualquier cosa, un diccionario, dentro de otro, etc.
# dicc = {"Costa Rica" : "San Jose", "Alemania":"Berlín", "España":"Madrid"}
# print(dicc)

# print("Podemso imprimir el valor, solo a apartir de la clave")
# print(dicc["España"])

# print("Se puede agregar nuevos elementos")
# dicc["Italia"] = "Managua"
# print(dicc)
# print("Podemos cambiar el valor de una clave, solo se sobreescribe")
# dicc["Italia"] = "Roma"
# print(dicc)
# print("Para eliminar un elemento lo haemos por su clave, usando del")
# del dicc["España"]
# print(dicc)

# #Clave y texto pueden ser cualquier tipo convinados
# print("Se le puede agregar varios elementso a una clave")
# prodicc ={1:"yo", 'x':'d',"objetos":["zapato", "carro", "sartén"]}
# print(prodicc)
# #Y se puede hacer lo mismo pero con un diccionario usando {}

# print(" keys devuleve todas las claves:", prodicc.keys())
# print("values nos da todo los valores: ", prodicc.values())
# print("len nos da la cantidad de elemntos: ", len(prodicc))

# # ==== Condicionales y cosas pro teclado ========
# print ("Prgama de evaluación de notas de alumnos")
# # Usamos input para que el teclado se quede esperando por lo que entro por llamada
# # Pero lo que estamso ingresando se toma como texto, hay que decirle que lo tome como numero
# # Por eso usamos int()
# nota_alumno= input()
# nota_alumno1= input("Ingrese nota del segundo alumno:")
# def evaluacion (nota):
#     valoracion = "aprobado"
#     if nota<5:
#         valoracion = "reprobado"
#     return valoracion

# print(evaluacion(int(nota_alumno)))
# print(evaluacion(int(nota_alumno1)))

# print("Verificación de acceso")
# edad = int(input("Introduzca su edad, pro favor: "))
# if edad < 18 :
#     print("No puedes pasar")
# elif edad > 100 :
#     print("Edad incorrecta")
# else:
#     print ("Puedes pasar")

# No puede haber dos else sin if, por eso isamos elif
# No existe switch en python
# Se pueden concatenar operadores de comparación
# funciona como si fuera un and
# edad= -7
# if 0<edad<100:
#     print("Edad es correcta")
# else:
#     print("Edad es incorrecta")

# salarioPres = int(input("Introduce salario presidente "))
# print("Salario de presidente: " + str(salarioPres))

# salariodirector= int(input("Introduce salario director "))
# print("Salario de presidente: " + str(salariodirector))


# salarioadministrativo= int(input("Introduce salario administrativo "))
# print("Salario de presidente: " + str(salarioadministrativo))

# if salarioadministrativo < salariodirector < salarioPres :
#         print("Todo bien")
# else:
#         print("Todo mal")




# algunos ejemplos de stings

nombre = input("Introduce tu nombre: ")
print("El nombre es: ", nombre)
print("El nombre es: ", nombre.capitalize())
print("El nombre es: ", nombre.casefold())
print("El nombre es: ", nombre.count(nombre))
print("El nombre es: ", nombre.isdigit())

# modulos 
# Es un archivo con extensión .py .pyc. Para modularizar y reutilizar código