# ==========================================
# Clase: Sesión 5 - Estructuras de Datos Secuenciales
# Tema: Métodos básicos de listas (append, insert, pop, remove)
# Autor: Prof. Adrián Torres
# ==========================================

# Las listas en Python vienen equipadas con "métodos", que son funciones 
# especiales integradas en la lista para manipular sus datos fácilmente.

print("")

# Empezamos con una lista de tareas para una plataforma web académica
TareasPlataforma: list[str] = ["Diseñar interfaz", "Configurar base de datos"]
print(f"Lista inicial: {TareasPlataforma}")

print("\n-------------\n")

# ==========================================
# 1. Agregar elementos: append() e insert()
# ==========================================
print("--- Agregando datos ---")

# append(): Agrega un elemento al FINAL de la lista. Es el método más usado.
TareasPlataforma.append("Programar backend en Python")
print(f"Después de append: {TareasPlataforma}")

# insert(): Agrega un elemento en una POSICIÓN específica (índice, valor).
# Los demás elementos se recorren hacia la derecha.
TareasPlataforma.insert(0, "Levantar requerimientos") 
print(f"Después de insert en índice 0: {TareasPlataforma}")

print("\n-------------\n")

# ==========================================
# 2. Eliminar elementos: pop() y remove()
# ==========================================
print("--- Eliminando datos ---")

# pop(): Elimina el elemento en la POSICIÓN indicada. 
# Si no le pasas ningún número, elimina y te devuelve el ÚLTIMO elemento.
TareaCompletada = TareasPlataforma.pop() 
print(f"Hicimos pop(). Se eliminó la tarea final: '{TareaCompletada}'")
print(f"Lista actual: {TareasPlataforma}")

# También podemos usar pop() con un índice específico
TareaPrioritaria = TareasPlataforma.pop(0)
print(f"Hicimos pop(0). Se eliminó la primera tarea: '{TareaPrioritaria}'")
print(f"Lista actual: {TareasPlataforma}")

print("\n")

# remove(): Elimina la primera coincidencia del VALOR exacto que le pasemos.
# Útil cuando sabes qué quieres borrar, pero no en qué posición está.
TareasPlataforma.append("Pruebas de usuario") # Agregamos algo para borrarlo
print(f"Lista antes de remove: {TareasPlataforma}")

TareasPlataforma.remove("Configurar base de datos")
print(f"Después de remove('Configurar base de datos'): {TareasPlataforma}")

print("\n-------------")
print("Fin de la Sesión 5.")