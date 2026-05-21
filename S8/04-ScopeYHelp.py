# ==========================================
# Clase: Sesión 8 - Funciones y Modularidad
# Tema: Ámbito de variables (Scope), Docstrings y la función help()
# Autor: Prof. Adrián Torres
# ==========================================

print("")
print("--- 1. Ámbito Global vs Ámbito Local ---")

# El "Scope" o ámbito dicta desde dónde podemos leer o modificar una variable.

# 1. VARIABLE GLOBAL: Declarada fuera de cualquier función. 
# Todo el programa puede verla.
NombreInstitucion = "Universidad Nacional Rosario Castellanos"

def mostrar_institucion():
    # Podemos acceder a variables globales desde adentro sin problema
    print(f"Leyendo global desde adentro: {NombreInstitucion}")
    
    # 2. VARIABLE LOCAL: Nace adentro de la función y muere al terminar la misma.
    CarreraActual = "Inteligencia Artificial"
    print(f"Leyendo local desde adentro: {CarreraActual}")

mostrar_institucion()

# Si intentamos imprimir la variable 'CarreraActual' aquí afuera, 
# Python arrojará un error (NameError) porque esa variable no existe en el ámbito global.
# print(CarreraActual)  <-- ESTO DARÍA ERROR

print("\n-------------------\n")

print("--- 2. Modificando variables globales (Uso de global) ---")

ContadorAuditorias = 0

def registrar_auditoria():
    # Para modificar una variable global desde adentro, debemos declararlo explícitamente
    # ¡Cuidado! Abusar de esto se considera una mala práctica arquitectónica.
    global ContadorAuditorias
    ContadorAuditorias += 1

registrar_auditoria()
registrar_auditoria()
print(f"Auditorías registradas (Global alterada): {ContadorAuditorias}")

print("\n-------------------\n")

print("--- 3. Docstrings y la función help() ---")

# Un "Docstring" (Cadena de Documentación) es el manual de instrucciones 
# que incrustamos justo debajo de la definición de nuestra función usando
# comillas triples (''' o """).

def procesar_calificaciones(notas: list[float]) -> float:
    """
    Calcula el promedio de una lista de calificaciones ignorando los ceros.
    
    Parámetros:
    notas (list[float]): Una lista con las calificaciones del alumno.
    
    Retorna:
    float: El promedio matemático exacto. Retorna 0.0 si la lista está vacía.
    
    Autor: Prof. Adrián Torres
    """
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)

# Cuando nosotros (o alguien de nuestro equipo) estemos programando y no recordemos
# qué hace una función, no necesitamos leer todo su código.
# Invocamos la función incorporada 'help()' y Python leerá el Docstring por nosotros.

print("Invocando el manual de nuestra función con help():\n")
help(procesar_calificaciones)

print("\n-------------")
print("Fin de la Sesión 8.")