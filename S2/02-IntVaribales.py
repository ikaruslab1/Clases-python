# ==========================================
# Clase: Sesión 2 - Tipos de datos
# Tema: Números Enteros (int) - Conceptos Básicos
# Autor: Prof. Adrián Torres
# ==========================================

# 'int' (Integer) representa números sin decimales.
# Pueden ser positivos, negativos o cero.

# 1. Declaración básica con Type Hinting
MiPrimerEntero: int = 42
EnteroNegativo: int = -15

print(f"Número positivo: {MiPrimerEntero}")
print(f"Número negativo: {EnteroNegativo}")

# Comprobación del tipo de dato
print(f"El tipo de {MiPrimerEntero} es: {type(MiPrimerEntero).__name__}")

# ==========================================
# Cambio de tipo de valor (Type Casting a int)
# ==========================================

print("\n-------------\n")

# CASO A: Convertir de texto (str) a entero (int)
# Útil cuando recibimos datos de un formulario o del usuario
TextoNumerico = "100"
NumeroConvertido = int(TextoNumerico)

print(f"El texto '{TextoNumerico}' ahora es un número: {NumeroConvertido}")
print(f"Nuevo tipo: {type(NumeroConvertido).__name__}")

# CASO B: Convertir de decimal (float) a entero (int)
# ¡Importante!: Python no redondea, solo elimina la parte decimal (trunca).
NumeroDecimal = 8.99
DecimalAEntero = int(NumeroDecimal)

print(f"El decimal {NumeroDecimal} convertido a entero es: {DecimalAEntero}")

# CASO C: Convertir de booleano (bool) a entero (int)
# Dato curioso para la clase: True vale 1 y False vale 0
VerdaderoEntero = int(True)
FalsoEntero = int(False)

print(f"True en entero es: {VerdaderoEntero}")
print(f"False en entero es: {FalsoEntero}")

print("\n-------------\n")