# ==========================================
# Clase: Sesión 7 - Estructuras de Datos de Mapeo
# Tema: Iteración sobre diccionarios usando métodos keys values e items
# Autor: Prof. Adrián Torres
# ==========================================

# A menudo necesitamos recorrer los diccionarios con un ciclo for para procesar
# masivamente la información contenida en ellos.

print("")

# Definimos las calificaciones de un alumno en la materia de inteligencia artificial.
Calificaciones = {
    "parcial_uno": 8.5,
    "parcial_dos": 9.0,
    "proyecto_final": 10.0
}

print("--- 1. Iterar usando el método keys ---")

# El método keys nos devuelve únicamente las claves del diccionario.
for Evaluacion in Calificaciones.keys():
    print(f"Criterio a evaluar: {Evaluacion}")

print("\n-------------------\n")

print("--- 2. Iterar usando el método values ---")

# El método values nos permite extraer directamente los valores almacenados
# ignorando cómo se llaman sus claves. Es útil para promedios o sumatorias.
SumaTotal = 0.0

for Nota in Calificaciones.values():
    print(f"Nota obtenida: {Nota}")
    SumaTotal += Nota

print(f"La sumatoria de las notas es: {SumaTotal}")

print("\n-------------------\n")

print("--- 3. Iterar usando el método items ---")

# El método items es el más poderoso porque nos devuelve la clave y el valor
# al mismo tiempo en cada ciclo. Requiere definir dos variables en el for.
for Evaluacion, Nota in Calificaciones.items():
    print(f"En la evaluación {Evaluacion} el alumno obtuvo un {Nota}")