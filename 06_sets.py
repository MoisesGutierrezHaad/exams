### sets

#1) Crea un set con los números del 1 al 5 e imprímelo.

sets = {1, 2, 3, 4, 5}

#2) Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.

sets = {1, 2, 3, 4, 5}
sets.add(6)
print (sets)

#3) Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?

sets = {1, 2, 3, 4, 5}  
sets.add(5)
print (sets) #los sets no repiten

#4) Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
verificar = {1, 2, 3, 4, 5}

print (3 in verificar)

#5) Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.

sets = {1, 2, 3, 4, 5}
sets.remove(4)

print (sets)

#6) Usa el método clear() para vaciar un set y luego imprime su longitud.

vaciar = {1, 324, 5, 23, 2, 123}
vaciar.clear()
print (len(vaciar)) 

#7) Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.

frutas = {"manzana", "naranja", "plátano"}
fruta = list(frutas)
print (fruta[0])

#8) Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.

primero = {1, 2, 3}
segundo = {4, 5, 6}

tercero = primero.union(segundo)
print (tercero)

#9) Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.

diferencia = {1, 2, 3, 4}
diferencia_2 = {3, 4, 5, 6}

la_diferencia = diferencia.difference(diferencia_2)

print (la_diferencia)

#10) Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.

se_va = {1, 2, 3, 4}
del se_va

print = se_va # NameError: name 'se_va' is not defined