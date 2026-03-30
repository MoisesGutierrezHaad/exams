#1) Imprime "¡Hola Mundo!" por consola.
print ("!Hola Mundo!") 

#2) Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1. 
#este codigo imprime !Hola Mundo!

#3) Imprime tu nombre y edad en la misma línea utilizando lafunción print.
print ("Mi nombre es Moises y tengo 28 años")

#4) Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.
print (type("esto es un texto")) #esto es un str
print (type (5)) #esto es un int
print (type (2.5)) #esto es un float

#5) Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.
"""
los tipos de datos son:
str = cadenas de texto
int = numeros enteros
float = numeros decimales
"""

#6) Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
x= "Hola "
y= "Mundo"

print (x + y)

#7) Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.

a = "Moises"
b = "28"

print ("Mi nombre es", a, "mi edad es", b, "años")

#8) Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.

c = input ("ingrese su nombre: ")

print ("Hola,", c, "!Bienvenido!")

#9) Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.

d = int (input("ingrese un primer: "))
e = int (input("ingrese un segundo: "))
f = (d+e)

print (f)
print (type(f))

#10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.
# asigne para variables d y e un valor para que asi la variable f haga la suma de ambos. por ultimo imprimo el valor de f y abajo el tipo de dato.