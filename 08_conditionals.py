#1) Escribe un programa que verifique si un número es positivo, negativo o cero.

la_condicion = int(input("ingrese el numero: "))

if la_condicion > 0:
    print ("es un numero positivo")
elif la_condicion == 0:
    print ("es un cero")
else: 
    print ("es un numero negativo")
    
#2) Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.

edad = int(input("ingrese su edad: "))

if edad > 18:
    print (f"es mayor de 18 años. tiene {edad} años de edad")

elif edad == 18: 
    print ("tiene 18 años es mayor de edad")

else:
    print("es menor de edad")  
    
#3) Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.

texto = input ("ingrese texto: ")

if not texto: 
    print ("esta vacia la cadena de texto")
else: 
    print ("no esta vacia la cadaena de texto")
    
#4) Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
numero_1 = int(input("ingrese primer numero: "))
numero_2 = int(input("ingrese segundo numero: "))

if numero_1 > numero_2: 
    print (f"primer numero ingresado {numero_1} es mayor que numero dos que es {numero_2}")
elif numero_1 == numero_2: 
    print (f"numeros ingresados son iguales {numero_1} = {numero_2}")
else:
    print (f"segundo numero {numero_2} es mayor que el primer numero ingresado {numero_1}")
    
#5) Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
numero = int(input("ingrese numero: "))

if numero %3 == 0 and numero %5 == 0:
    print (f"numero {numero} si es divisible")
else:
    print (f"numero {numero} no es divisible entre 3 y 5 al tiempo")

#6) Solicita al usuario que ingrese un número y verifica si es par o impar.
ingrese_numero = int(input("ingrese numero: "))

if ingrese_numero %2 == 0:
    print (f"numero {ingrese_numero} es par")
else:
    print (f"numero {ingrese_numero} no es par")

#7) Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
puede_votar = int(input("que edad tienes: "))

if puede_votar >= 18: 
    print ("puede votar")
elif puede_votar >= 16:
    print ("puede votar con permiso")
else: 
    print ("no puede votar")

#8) Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
contraseña = {1421, 1820}
ingrese_contraseña = int(input("ingrese contaseña: "))
if contraseña == ingrese_contraseña: 
    print ("contraseña correcta")
else: 
    print ("ERROR: no coincide contraseña")

#9) Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).

numero = int(input("ingrese el numero: "))

if 10 <= numero <= 20:
    print (f"numero {numero} esta entre 10 y 20")
else: 
    print("numero no esta entre 10 a 20")

#10) Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

semaforo = str(input("ingrese uno de los 3 colores (rojo, amarillo o verde): ")).lower()

if semaforo == "rojo":
    print ("Detenerse")
    
elif semaforo == "amarillo":
    print ("Estar alerta")

elif semaforo == "Verde":
    print ("Avanzar")
    
else: 
    print ("ingreso un color no valido")