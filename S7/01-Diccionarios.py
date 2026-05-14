# ==========================================
# Clase: Sesión 7 - Estructuras de Datos de Mapeo
# Tema: Diccionarios y operaciones de acceso modificación y eliminación
# Autor: Prof. Adrián Torres
# ==========================================

# Los diccionarios almacenan información vinculando una clave única con un valor específico.
# Esta estructura es muy utilizada en bases de datos y formatos como json.

print("")
print("--- 1. Creación y estructura de pares clave-valor ---")

# Declaramos un diccionario sobre un modelo de lenguaje.
# Las claves suelen ser cadenas de texto y los valores pueden ser cualquier tipo de dato.
ModeloLenguaje = {
    "nombre": "transformer",
    "parametros": 7000000000,
    "entrenado": True
}

print(f"Información del modelo: {ModeloLenguaje}")
print(f"Tipo de dato: {type(ModeloLenguaje).__name__}")

print("\n-------------------\n")

print("--- 2. Operaciones de acceso ---")

# Para acceder a un valor específico usamos corchetes con el nombre de la clave.
NombreDelModelo = ModeloLenguaje["nombre"]
print(f"El nombre del modelo es: {NombreDelModelo}")

# Una forma más segura de acceder es emplear el método get el cual evita errores
# si la clave no existe en el diccionario.
TasaAprendizaje = ModeloLenguaje.get("tasa_aprendizaje", "Clave no encontrada")
print(f"Tasa de aprendizaje: {TasaAprendizaje}")

print("\n-------------------\n")

print("--- 3. Modificación y eliminación ---")

# Modificar es tan sencillo como reasignar un valor a una clave existente.
ModeloLenguaje["entrenado"] = False
print(f"Estado de entrenamiento actualizado: {ModeloLenguaje['entrenado']}")

# Para agregar un nuevo par clave-valor simplemente asignamos datos a una clave nueva.
ModeloLenguaje["version"] = 2.0
print(f"Diccionario con nuevo dato: {ModeloLenguaje}")

# Para eliminar un elemento utilizamos el método pop indicando la clave.
DatoEliminado = ModeloLenguaje.pop("parametros")
print(f"Se eliminó la clave parametros con el valor: {DatoEliminado}")
print(f"Diccionario final: {ModeloLenguaje}")