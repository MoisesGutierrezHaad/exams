#1) Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting (name ="desconocido"):
    print (f"hola, {name}")
    
personalized_greeting("Moises")

#2) Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiply (numero_1, numero_2):
    print (numero_1 * numero_2)

multiply (2, 7) 

#3) Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.

def is_even(numero):
    return numero %2 == 0

print (is_even(16)) #true
print (is_even(7)) #false

#4) Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas. 

def convert_to_uppercase(texto):
    return texto.upper()

print (convert_to_uppercase("ian"))

#5) Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.

def arbitrary_sum(*numeros):
    return sum(numeros)

#6) Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting (name, surname):
    return f"Hola, {name} {surname}"

#7) Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente. 
def power(base, exponente):
    return base ** exponente

#8) Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio. 

def calculate_average(numero1, numero2 , numero3):
    return (numero1, numero2, numero3 / 3)

#9) Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene. 
def count_characters(texto):
    return len(texto)

#10) Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado. 

def display_messages(*mensajes):
    for mensaje in mensajes: 
        print (mensaje.upper())
        