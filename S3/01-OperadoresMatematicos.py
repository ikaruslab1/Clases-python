# ==========================================
# Clase: Sesión 3 - Operadores
# Tema: Matemáticos
# Autor: Prof. Adrián Torres
# ==========================================

# Los operadores matemáticos nos permiten realizar cálculos básicos y 
# operaciones aritméticas sobre valores numéricos (int, float).

# Definimos dos variables iniciales para nuestros ejemplos
a = 15
b = 4

print(f"--- Valores iniciales: a = {a}, b = {b} ---\n")

# 1. Suma (+)
suma = a + b
print(f"Suma (a + b): {suma}")

# 2. Resta (-)
resta = a - b
print(f"Resta (a - b): {resta}")

# 3. Multiplicación (*)
multiplicacion = a * b
print(f"Multiplicación (a * b): {multiplicacion}")

# 4. División (/) 
# Nota: En Python 3, la división simple SIEMPRE devuelve un número flotante (float)
division = a / b
print(f"División (a / b): {division}")

# 5. División entera (//)
# Devuelve únicamente la parte entera del cociente, descartando los decimales.
division_entera = a // b
print(f"División entera (a // b): {division_entera}")

# 6. Módulo (%)
# Devuelve el "resto" o residuo de una división. Es muy útil para saber si un 
# número es par (ej. numero % 2 == 0).
modulo = a % b
print(f"Módulo o Resto (a % b): {modulo}")

# 7. Exponenciación (**)
# Eleva el primer número a la potencia del segundo número.
potencia = a ** b
print(f"Exponenciación (a ** b): {potencia}")