# ==========================================
# Clase: Sesión 2 - Tipos de datos
# Tema: Decimales (float) en Python
# Autor: Prof. Adrián Torres
# ==========================================

# 'float' hace referencia a "Floating point" (Coma flotante).
# Es el tipo de dato que usamos para números que tienen una parte fraccionaria o decimal.

print("")

# Declaración de una variable float.
# Usamos ': float' como Pista de Tipo (Type Hinting).
# ¡Importante!: En Python (y en programación en general), los decimales
# se separan con un punto (.), NUNCA con una coma (,).
PrecioArticulo: float = 99.99
Temperatura: float = -5.5

print(f"El precio es ${PrecioArticulo} y el tipo es: {type(PrecioArticulo).__name__}")

# ==========================================
# Notación Científica (Muy útil en Ingeniería / IA)
# ==========================================

print("\n-------------\n")

# Python permite declarar floats usando notación científica con la letra 'e'.
# Esto es muy útil para números extremadamente grandes o muy pequeños.

# 2.5e3 significa 2.5 x 10^3 (es decir, 2500.0)
NumeroGrande = 2.5e3 
print(f"Notación científica 2.5e3 equivale a: {NumeroGrande}")

# 1.5e-4 significa 1.5 x 10^-4 (es decir, 0.00015)
NumeroPequeno = 1.5e-4
print(f"Notación científica 1.5e-4 equivale a: {NumeroPequeno}")

# ==========================================
# Cambio de tipo de valor (Type Casting a float)
# ==========================================

print("\n-------------\n")

# Podemos convertir enteros y textos a decimales usando la función float()

# De 'int' a 'float' (Simplemente le añade el .0)
Entero = 10
EnteroAFloat = float(Entero)
print(f"El entero {Entero} convertido a float es: {EnteroAFloat}")

# De 'str' a 'float' (El texto debe tener formato de número válido)
TextoDecimal = "3.14159"
TextoAFloat = float(TextoDecimal)
print(f"El texto convertido a float permite sumar: {TextoAFloat + 1} ")