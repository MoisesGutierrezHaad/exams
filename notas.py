Para guardar un valor específico en un diccionario de Python, se utiliza la sintaxis nombre_diccionario["clave"] = valor, donde la clave debe ser un objeto inmutable (como un string, número o tupla). 

Métodos de almacenamiento y persistencia
Asignación directa en memoria: Puedes agregar o modificar un par clave-valor simplemente asignando un valor a una nueva clave o sobreescribiendo una existente. Por ejemplo, mi_dicc["Italia"] = "Roma" asigna el valor "Roma" a la clave "Italia". 
Persistencia con Pickle: Para guardar el diccionario en un archivo binario y recuperarlo en futuras sesiones, se utiliza el módulo pickle. El código pickle.dump(mi_dicc, archivo) guarda el objeto completo, mientras que pickle.load(archivo) lo restaura. 
Persistencia con JSON: Si necesitas un formato legible y compatible con otros lenguajes, el módulo json permite exportar el diccionario usando json.dump(mi_dicc, archivo), aunque requiere que los datos sean serializables a texto plano. 
Ejemplo de código
import pickle
import json

# 1. Crear y guardar un valor específico
mi_dicc = {}
mi_dicc["nombre"] = "Juan"
mi_dicc["edad"] = 30

# 2. Guardar en archivo binario (Pickle)
with open("datos.pkl", "wb") as f:
    pickle.dump(mi_dicc, f)

# 3. Guardar en archivo de texto (JSON)
with open("datos.json", "w") as f:
    json.dump(mi_dicc, f)

# 4. Cargar de nuevo (Ejemplo con Pickle)
with open("datos.pkl", "rb") as f:
    mi_dicc_cargado = pickle.load(f)

Consideraciones clave
Las claves deben ser inmutables; no se pueden usar listas como claves, pero sí tuplas. 
Si asignas un valor a una clave que ya existe, el valor anterior se pierde y es reemplazado. 
El formato Pickle es rápido y soporta cualquier objeto de Python, pero no es legible manualmente. 
El formato JSON es legible pero limitado a tipos de datos estándar (cadenas, números, listas, diccionarios, booleanos y nulo). 
