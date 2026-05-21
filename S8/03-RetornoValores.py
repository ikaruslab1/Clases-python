# ==========================================
# Clase: Sesión 8 - Funciones y Modularidad
# Tema: Retorno de información mediante return
# Autor: Prof. Adrián Torres
# ==========================================

# Hasta ahora, nuestras funciones solo imprimen texto en la terminal (print).
# Pero en sistemas reales, una función procesa datos y DEBE devolver un resultado
# para que el programa pueda seguir trabajando con él. Para esto usamos 'return'.

print("")
print("--- 1. La palabra reservada return ---")

# Usamos la flecha '->' para indicar con Type Hinting qué tipo de dato
# va a devolver la función. En este caso, devolverá un float.
def calcular_promedio(calificacion1: float, calificacion2: float) -> float:
    suma = calificacion1 + calificacion2
    promedio = suma / 2
    return promedio  # La función termina aquí y "escupe" este valor al exterior.
    
    # IMPORTANTE: Cualquier código escrito después de un 'return' jamás se ejecutará.
    print("Esto nunca se imprimirá.")

# El valor retornado lo podemos guardar directamente en una variable
PromedioSemestre = calcular_promedio(9.5, 8.0)
print(f"El cálculo ha finalizado. El promedio obtenido es: {PromedioSemestre}")

print("\n-------------------\n")

print("--- 2. Retorno Múltiple (Tuplas implícitas) ---")

# Python tiene una característica fantástica: puede retornar múltiples valores 
# en una sola línea. Lo que hace internamente es agruparlos en una Tupla.

def extraer_dimensiones_imagen() -> tuple:
    ancho = 1920
    alto = 1080
    canales_color = 3 # RGB
    return ancho, alto, canales_color

# Podemos guardar todo en una variable (como tupla) o "desempaquetarlo" en 3 variables
Dimensiones = extraer_dimensiones_imagen()
print(f"Dimensiones crudas (Tupla): {Dimensiones}")

w, h, c = extraer_dimensiones_imagen()
print(f"Desempaquetado: Ancho {w}px, Alto {h}px, Canales {c}")

print("\n-------------------\n")

print("--- 3. Return Temprano (Guard Clauses) ---")

# Un patrón de diseño profesional es usar el return para abortar una función
# si no se cumplen ciertas condiciones, evitando anidar demasiados if-else.

def validar_edad_acceso(edad: int) -> str:
    if edad <= 0:
        return "Error: La edad no puede ser cero o negativa." # Corta la ejecución
    
    if edad < 18:
        return "Acceso denegado: Menor de edad." # Corta la ejecución
        
    return "Acceso concedido al sistema de tutorías." # Camino feliz

print(f"Prueba 1: {validar_edad_acceso(-5)}")
print(f"Prueba 2: {validar_edad_acceso(27)}")