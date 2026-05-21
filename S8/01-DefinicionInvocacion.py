# ==========================================
# Clase: Sesión 8 - Funciones y Modularidad
# Tema: Definición e invocación de funciones propias (def)
# Autor: Prof. Adrián Torres
# ==========================================

# A medida que nuestros programas crecen, escribir el mismo código una y otra vez 
# se vuelve insostenible. Las funciones nos permiten encapsular bloques de código 
# bajo un nombre para reutilizarlos (Principio DRY: Don't Repeat Yourself).

print("")
print("--- 1. Definiendo nuestra primera función ---")

# Utilizamos la palabra reservada 'def' (define) seguida del nombre de la función
# y paréntesis (). Los dos puntos ':' indican que inicia el bloque de código.
# Nota: La convención en Python es nombrar a las funciones en minúsculas y 
# separadas por guiones bajos (snake_case) o PascalCase, dependiendo el estándar.

def iniciar_sistema():
    print("Inicializando bases de datos de la universidad...")
    print("Cargando módulos de Inteligencia Artificial...")
    print("¡Sistema listo y operando al 100%!")

# Si ejecutamos el programa hasta aquí, no pasará nada. 
# Hemos "definido" qué hace la función, pero no le hemos ordenado que lo haga.

print("Definición completada, pero no invocada aún.")

print("\n-------------------\n")

print("--- 2. Invocación (Llamada) a la función ---")

# Para que el bloque de código se ejecute, debemos "llamar" o "invocar" a la función
# escribiendo su nombre seguido de paréntesis.

print("Llamando a la función por primera vez:")
iniciar_sistema()

print("\nLlamando a la función por segunda vez (reusabilidad):")
iniciar_sistema()

print("\n-------------------\n")

print("--- 3. Funciones vacías (pass) ---")

# En ocasiones estamos diseñando la arquitectura de nuestro software y 
# sabemos qué funciones necesitaremos, pero aún no queremos programar su lógica.
# Para evitar errores de sintaxis al dejar el bloque vacío, usamos 'pass'.

def entrenar_red_neuronal():
    pass  # Le dice a Python: "No hagas nada por ahora, volveré a esto luego"

print("La función 'entrenar_red_neuronal' existe, pero no ejecuta nada gracias a 'pass'.")