#1) Usa un bucle while para imprimir los números del 1 al 10.

interador = 1

while interador <= 10:
    print (interador)
    interador += 1
    
#2) Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.

numeros = [10, 20, 30, 40, 50]

for numero in numeros: 
    print(numero)
    
#3 ) Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.

numeros = 1
sum = 0

while numeros <= 100:
    numeros += 1
    sum += 1
    
    print (sum)
    
#4) Escribe un bucle for que imprima cada carácter de la cadena “Python”. 

palabra = ("Python")

for letras in palabra: 
    print (letras)
    
#5) Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.  

x = 0

while x <= 50: 
    if x % 7 == 0:
        print (x)
        break
    x+=1
    print (x)
    
#6) Usa un bucle for para recorrer el diccionario {“name”: “Brais”, “age”: 37, “country”: “Galicia”} e imprime las claves.

diccionario = {
    "name" : "Brais",
    "age" : 37,
    "country" : "Galicia",
}

for llaves in diccionario:
    print (llaves) 

#7) Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.

pares = 0

while pares <= 20:
    if pares % 2 == 0: 
        print(pares)
    pares += 1
    
#8) Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso. 

for i in range(10, 0, -1):
    print (i)
    
#9) Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].

contar = [30, 10, 30, 20, 30, 40]
numero = 0

for repeticion in contar: 
    if repeticion == 30:
        numero += 1
print (numero)

# 10) Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre “Brais”.  

nombres = ["ian", "katherine", "johan", "Brais", "Thary"]

for recorre in nombres:
    if recorre == "Brais":
        print ("Aqui esta Brais")
        break
    print (nombres)