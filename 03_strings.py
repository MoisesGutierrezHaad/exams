my_strings = "este es un \nsalto de linea"

print (my_strings)

my_strings = "\tahora este es con tabulacion"

print (my_strings)

my_strings = "\\tahora este es con \\nescapado"

print (my_strings)

# Formateo 

name, surname, age = "Moises", "gutierrez", 28

print ("mi nombre es %s y mi apellido es %s tengo %s años".format(name, surname, age))
print ("mi nombre es {} y mi apellido es {} tengo {} años".format(name, surname, age))
print ("mi nombre es %s y mi apellido es %s tengo %d años" %(name, surname, age))
print (f"mi nombre es {name} y mi apellido es {surname} tengo {age} años") #a esta forma se le llama inferencia de datos 

#desempaquetado de caracteres

language = "python"

a, b, c, d, e, f = language

print (a)
print (b)
print (c)
print (d)
print (e)
print (f)

#division

language_slice = language [1:3]
print (language_slice)

language_slice = language [1:]
print (language_slice)

language_slice = language [-2]
print (language_slice)

#reverse
reversed_language = language [:: -1]
print (reversed_language)

#funciones 
print (language.capitalize()) #pone la primera letra en mayusculas.
print (language.upper()) #convierte el texto a mayuscullas
print (language.count("t")) #verifica cuantas letras en especifico estan en el texto
print (language.isnumeric()) #verifica si es un numero false ya que es str
print ("1".isnumeric()) #verifica que es numero true es un numero 
print (language.lower()) #convierte en minusculas todo
print (language.upper().isupper()) #verifica que todo este en mayusculas true por el .upper
print (language.lower().isupper()) #verifica que es mayusculas false por .lower
print (language.startswith("Py")) #verifica si comienza con letras especificas Py false por que cuenta minusculas o mayusculas
print (language.startswith("py")) #verifica si comienza con letras especificas py true por que cuenta miscunulas donde si empieza asi 

#1) Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Python"
print (len(text))

#2) Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.

print ("Hola" + " " + "Python")

#3) Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.

print ("resultado del \n del ejercicio")

#4) Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

nombre, apellido, edad = "Moises", "Gutierrez", 28

print (f"Me llamo {nombre} {apellido} y yo tengo {edad} años")
print ("Me llamo %s %s y yo tengo %d años" %(nombre, apellido, edad))

#5) Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.

palabra = "Python"

a, b, c, d, e, f = palabra

print (a)
print (b)
print (c)
print (d)
print (e)
print (f)

#6) Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7

x = "Programacion"

programacion_slice = x [3:7]

print (programacion_slice)

#7) Invierte la cadena “Python” usando slicing y muestra el resultado.

cadena = "Python"
reversa_cadena = cadena [:: -1]

print (reversa_cadena)

#8) Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.

print ("aprendiendo python".upper())

#9) Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.

print ("Programacion en Python".count("n"))

#10) Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.

print ("12345".isnumeric()) 
