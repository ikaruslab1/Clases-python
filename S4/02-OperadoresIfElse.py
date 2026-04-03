# ==========================================
# Clase: Sesión 4 - Control de Flujo
# Tema: Operadores Lógicos (and, or, not)
# Autor: Prof. Adrián Torres
# ==========================================

# Los operadores lógicos nos permiten combinar múltiples condiciones
# en una sola evaluación.

print("")

# Variables booleanas (bool) para nuestros ejemplos
EsEstudianteUNRC: bool = True
TieneCredencialVigente: bool = False
PromedioIA: float = 9.2

# ==========================================
# 1. Operador 'and' (Y)
# ==========================================
# Para que la condición completa sea Verdadera, TODAS las partes deben ser Verdaderas.

print("--- Evaluación con 'and' ---")
if EsEstudianteUNRC and TieneCredencialVigente:
    print("Puedes solicitar el préstamo de libros en la biblioteca.")
else:
    print("No puedes solicitar libros. Revisa tu inscripción o credencial.")

print("\n-------------\n")



# ==========================================
# 2. Operador 'or' (O)
# ==========================================
# Para que la condición sea Verdadera, basta con que UNA de las partes sea Verdadera.

print("--- Evaluación con 'or' ---")
# Supongamos que damos una beca si es estudiante de la facultad O si tiene un promedio de excelencia.
if EsEstudianteUNRC or PromedioIA > 9.0:
    print("Eres candidato a la beca de investigación.")
else:
    print("No cumples con los requisitos para la beca en este momento.")

print("\n-------------\n")



# ==========================================
# 3. Operador 'not' (NO / Negación)
# ==========================================
# Invierte el valor de la condición. Lo Verdadero se hace Falso y viceversa.

print("--- Evaluación con 'not' ---")
SistemaEnMantenimiento: bool = False

# "Si el sistema NO está en mantenimiento..."
if not SistemaEnMantenimiento:
    print("El servidor está en línea. Puedes subir tu práctica de código.")
else:
    print("El servidor está caído por mantenimiento. Intenta más tarde.")