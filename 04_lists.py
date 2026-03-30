### lists: es un conjunto de datos. 

my_list = list()
my_other_list = []

print (len(my_list))
print (len(my_other_list))

my_list = [35, 21, 53, 72, 12, 32, 35]
my_list.sort()
print (my_list) 

my_list.reverse()
print (my_list)

my_list.clear()
print(my_list)


# Eliminar y devolver el último elemento
frutas = ['manzana', 'banana', 'cereza']
ultimo = frutas.pop(0) #
frutas.append(ultimo)
print(ultimo)  # Salida: 'cereza'
print(frutas)  # Salida: ['manzana', 'banana']

# Eliminar y devolver un elemento en una posición específica
numeros = [10, 20, 30, 40]
eliminado = numeros.pop(1)
print(eliminado)  # Salida: 20
print(numeros)    # Salida: [10, 30, 40]   

#1) Crea una lista con los números del 1 al 5 e imprímela.

numbers = [1, 2, 3, 4, 5]
print (numbers)

#2) Accede e imprime el tercer elemento de la lista [10, 20,30, 40, 50].
numbers = [10, 20,30, 40, 50]
print (numbers[2])

#3) Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print (numbers)

#4) Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].

numeros = [10, 20, 30, 40, 50]
numeros.insert(2, 15)
print (numeros)

#5) Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].

numero = [10, 20, 30, 30, 40, 50]
numero.remove(30)
print (numero)

#6) Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.

lista = [1, 2, 3, 4, 5]
eliminado = lista.pop()
print (lista)
print (eliminado)

#7) Invierte la lista [100, 200, 300, 400, 500] e imprímela.

ciens = [100, 200, 300, 400, 500]
ciens.reverse()
print (ciens)

#8) Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.

desorden = [3, 1, 4, 2, 5]
desorden.sort()
print (desorden)

#9) Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.

goku = [1, 2, 3]
vegeta = [4, 5, 6]
gogeta = goku + vegeta
print (gogeta)

#10) Crea una sublista con los elementos de la lista (10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
numeros = [10, 20, 30, 40, 50]
nuevos_numeros = numeros[1:3]
print(nuevos_numeros)