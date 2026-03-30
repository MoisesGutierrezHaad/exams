### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print (type(my_dict))
print (type(my_other_dict))

my_other_dict = {"nombre": "moises", "apellido": "gutierrez", "edad" : 28, 1: "python"}
my_dict = {
    "nombre": "moises", 
    "apellido": "gutierrez", 
    "edad" : 28, 
    "lenguajes":{"python", "c++", "html"},
    1: 1.81
}
 
print (my_dict)
print (my_other_dict)

print (len(my_other_dict))
print (len(my_dict))

print (my_dict["lenguajes"])

my_dict ["nombre"] = "Pedro"
print (my_dict)

my_dict ["direccion"] =  "calle 33 # 8-82"
print (my_dict)

del my_dict ["direccion"]
print (my_dict)

print ("lenguajes" in my_dict)

print (my_dict.items())
print (my_dict.keys())
print (my_dict.values())
my_new_dict = my_dict.fromkeys(("nombre", 1)) #crea un nuevo diccionario sin valores
print (my_new_dict)

#1) Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

diccionario = {
    "name" : "Moises",
    "age" : 28,
    "country" : "ciudad",
}
print (diccionario)

#2) Accede al valor de la clave name en el diccionario.

print (diccionario["name"])

#3) Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado. 

diccionario ["job"] = "Programador"
print (diccionario)

#4) Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.

diccionario ["age"] = "38"
print (diccionario)

#5) Elimina la clave country del diccionario e imprime el diccionario resultante.

del diccionario ["country"]
print (diccionario)

#6) Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

numeros = {
    1 : (1*1),
    2 : (2*2),
    3 : (3*3),
    4 : (4*4),
    5 : (5*5)
}
print (numeros)

#7)Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
clave = {"name": "Brais", "age": 37, "country": "Galicia"}

print ("age" in clave)

#8) Imprime solo las claves del diccionario. 

print (clave.keys())

#9) Convierte las claves del diccionario en una lista e imprime la lista resultante.
print (list(diccionario.keys()))

#10) Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

llaves = ["name", "age", "job"]
new_llaves = dict.fromkeys(llaves, "Desconocido")
print (new_llaves)