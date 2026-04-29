# ==========================================
# Clase: Sesión 5 - Estructuras de Datos Secuenciales
# Tema: Listas (list), Mutabilidad y función len()
# Autor: Prof. Adrián Torres
# ==========================================

# Hasta ahora hemos guardado un solo valor por variable.
# Las listas (list) nos permiten almacenar una secuencia de múltiples valores
# en una sola variable. Se definen utilizando corchetes [ ].

print("")

# ==========================================
# 1. Declaración de Listas y la función len()
# ==========================================

# Con Type Hinting podemos especificar que es una lista y qué tipo de datos contiene.
ModelosDeIA: list[str] = ["Regresión Lineal", "Árboles de Decisión", "Redes Neuronales"]
Calificaciones: list[float] = [8.5, 9.2, 7.8, 10.0]

print("--- Explorando Listas ---")
print(f"Lista de modelos: {ModelosDeIA}")
print(f"Tipo de dato: {type(ModelosDeIA).__name__}")

# La función incorporada len() (de "length", longitud) es fundamental.
# Nos dice cuántos elementos exactos hay dentro de nuestra secuencia.
# Esto es vital para evitar errores al recorrer datos estructurados o matrices.
TotalModelos = len(ModelosDeIA)
print(f"¿Cuántos modelos tenemos en la lista?: {TotalModelos}")

print("\n-------------\n")

# ==========================================
# 2. Mutabilidad (Capacidad de cambiar)
# ==========================================

# Las listas son MUTABLES. Esto significa que podemos modificar, alterar 
# o reemplazar sus elementos internos una vez que la lista ya fue creada,
# sin necesidad de crear una variable nueva.

print("--- Mutabilidad en acción ---")
ProgramasEducativos: list[str] = ["Actuaría", "Relaciones Internacionales", "Derecho"]
print(f"Lista original: {ProgramasEducativos}")

# Para modificar un elemento, accedemos a su posición (índice) y le asignamos un nuevo valor.
# ¡Ojo! En Python, y en la programación en general, empezamos a contar desde el CERO (0).
# Posición 0: "Actuaría", Posición 1: "Relaciones Internacionales", Posición 2: "Derecho".

ProgramasEducativos[2] = "Inteligencia Artificial"
print(f"Lista modificada: {ProgramasEducativos}")

# Como vemos, el elemento en la posición 2 ("Derecho") fue reemplazado.