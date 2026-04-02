# ==========================================
# Clase: Sesión 3 - Operadores
# Tema: Asignación
# Autor: Prof. Adrián Torres
# ==========================================

# Se utilizan para asignar valores a las variables. Python permite combinar 
# operaciones matemáticas básicas directamente con la asignación para hacer 
# el código más corto y limpio.

# 1. Asignación básica (=)
x = 10
print(f"Asignación inicial: x = {x}")

# 2. Asignación de suma (+=)
# Es exactamente lo mismo que hacer: x = x + 5
x += 5  
print(f"Suma en asignación (x += 5): x = {x}")

# 3. Asignación de resta (-=)
# Es exactamente lo mismo que hacer: x = x - 3
x -= 3  
print(f"Resta en asignación (x -= 3): x = {x}")

# 4. Asignación de multiplicación (*=)
x *= 2  
print(f"Multiplicación en asignación (x *= 2): x = {x}")

# 5. Asignación de división (/=)
x /= 4  
print(f"División en asignación (x /= 4): x = {x}") # x se convierte en float

# 6. Asignación de módulo (%=)
# Toma el valor actual de x, lo divide por 3 y guarda el residuo en x
x %= 3  
print(f"Módulo en asignación (x %= 3): x = {x}")

# 7. Asignación de exponente (**=)
z = 5
z **= 2 # z = z ** 2
print(f"\nNueva variable z = 5")
print(f"Exponente en asignación (z **= 2): z = {z}")