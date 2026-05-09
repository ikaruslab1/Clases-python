# ==========================================
# Clase: Sesión 6 - Ciclos e Iteraciones
# Tema: Ciclo while y condiciones de salida
# Autor: Prof. Adrián Torres
# ==========================================

# Un ciclo 'while' (mientras) nos permite repetir un bloque de código
# SIEMPRE Y CUANDO una condición siga siendo Verdadera (True).

print("")

# ==========================================
# 1. Estructura básica de un ciclo while
# ==========================================
print("--- 1. Contador Básico ---")

Contador: int = 1
Limite: int = 5

# Leemos esto como: "Mientras el Contador sea menor o igual al Límite..."
while Contador <= Limite:
    print(f"Iteración actual: {Contador}")
    
    # ¡CRÍTICO! Debemos modificar la variable de control en cada iteración
    # para eventualmente alcanzar la condición de salida.
    # Si olvidamos esto, crearemos un "Ciclo Infinito" que colapsará el programa.
    Contador += 1 

print("El ciclo ha terminado.")

print("\n-------------\n")

# ==========================================
# 2. Ciclo while dependiente del usuario
# ==========================================
print("--- 2. Condición controlada por entrada ---")

# Podemos usar un while para mantener un programa ejecutándose hasta
# que el usuario decida detenerlo de forma explícita.

Continuar: bool = True
Intentos: int = 0

print("Simulando un sistema de validación...")

while Continuar:
    Intentos += 1
    # Simulamos que después de 3 intentos el sistema de seguridad detiene el proceso
    if Intentos >= 3:
        print(f"Se alcanzó el máximo de {Intentos} intentos permitidos. Saliendo...")
        Continuar = False  # Cambiamos la condición de salida a False
    else:
        print(f"Intento {Intentos} procesado. Ejecutando de nuevo...")

print("\n-------------")
print("Fin del Tema 1.")