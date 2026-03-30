#variables

# 1. Declara y asigna valores a las siguientes variables:

name = "Moises"

age = 28

height = 1.81

print (name)

print (age)

print (height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuantos años tienes.

age = str(age) #la convierto a str

print ("mi edad es,", age, "años de edad") #concateno

print (type(age))#verico si, lo cambio a str.

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segun corresponda e impri­mela.

is_student = True

print ("¿Eres estudiante?", is_student)

# 4. Usa la funcion len() para calcular cuantos caracteres tiene tu nombre completo, almacenado en una variable.

name = "Moises"

print (len(name))

# 5. Declara tres variables en una sola li­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

nombre, apellido, ciudad = "Moises", "Gutierrez", "Barranquilla"

print ("Soy de", ciudad, "y me llamo", nombre, apellido,".")

# 6. Usa la funcion input() para solicitar al usuario su color favorito y almacenalo en una variable color. Luego, imprime el valor ingresado.

color_favorito = input ("Ingrese su color favorito: ")

print ("tu color favorito es el:", color_favorito)

# 7. Declara una variable fruit e iniciala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

fruit = ("pera")

print (fruit)

fruit = ("manzana")

print (fruit)

# 8. Convierte un numero decimal, almacenado en la variable price, a un numero entero y luego imprimelo.

price = 2.000

price = int(price)

print (price)

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direccion usando la funcion len(). Imprime el resultado.

addres = "calle 33 # 8-82 barranquilla"

addres_len = len(addres)

print (addres_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurandote de que siempre sera¡ un numero. Luego, cambia su valor a un numero diferente y verifica el tipo de la variable con type().

phone: int = 3007647144
print (type(phone))
phone = 3185773194
print (type(phone))