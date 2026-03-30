####Tuples

#1) Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.

valores = (10, 20, 30, 40, 50)
print (valores)

#2) Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.

elemento = (100, 200, 300, 400, 500)
print (elemento[5])

#3) Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

#modificar = (1, 2, 3)
#modificar [0] = 10 # TypeError: 'tuple' object does not support item assignment

#4) Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

numero = (1, 2, 3, 3, 4, 5, 3)
print (numero.count(3))

#5) Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

cadena = ("Java", "Python", "JavaScript", "Python")
print (cadena.index("Python"))

#6) Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

lunala = (1, 2, 3)
sol_galeo = (4, 5, 6)

necrozma = lunala + sol_galeo

print (necrozma)

#7) Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

tupla = (10, 20, 30, 40, 50)
sub_tupla = tupla[2:4]

print (sub_tupla)

#8) Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

colors = ("rojo", "verde", "azul")
lista_de_colores = list(colors)
lista_de_colores[1] = "amarillo"
convertida = tuple(lista_de_colores)
print(convertida)

#9) Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

my_tuple = (1, 2, 3, 4)

del my_tuple

print (my_tuple) #NameError: name 'my_tuple' is not defined

#10) Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.

elemento = (100, )

print (elemento)