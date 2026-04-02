# ==========================================
# Clase: Sesión 2 - Tipos de datos
# Tema: Booleanos (bool) en Python
# Autor: Prof. Adrián Torres
# ==========================================

# 'bool' hace referencia a la palabra Boolean (Booleano).
# Es el tipo de dato más simple y fundamental: solo puede tener dos valores.
# Verdadero (True) o Falso (False). 
# Son la base de la toma de decisiones en la programación.

print("")

# Declaración de una variable booleana.
# Usamos ': bool' como Pista de Tipo (Type Hinting).
# ¡Dato crítico!: En Python, True y False SIEMPRE deben escribirse con mayúscula inicial.
SistemaEncendido: bool = True
SistemaApagado: bool = False

print(f"El estado del sistema es Encendido: {SistemaEncendido}")
print(f"El tipo de dato es: {type(SistemaEncendido).__name__}")

# ==========================================
# ¿De dónde nacen los booleanos? (Comparaciones)
# ==========================================

print("\n-------------\n")

# Normalmente no escribimos "True" o "False" directamente.
# Los booleanos suelen ser el resultado de comparar datos.
NumeroA = 10
NumeroB = 5

# Le preguntamos a Python: "¿A es mayor que B?". Nos responderá con un booleano.
EsMayor = NumeroA > NumeroB
print(f"¿10 es mayor que 5? -> {EsMayor}")

# Otras comparaciones comunes que generan booleanos:
print(f"¿10 es menor que 5? -> {NumeroA < NumeroB}")

# Usamos doble igual '==' para comparar si dos cosas son idénticas 
# (Recuerda: un solo '=' sirve para guardar valores en variables).
print(f"¿10 es exactamente igual a 5? -> {NumeroA == NumeroB}") 

# El símbolo '!=' significa "es diferente de"
print(f"¿10 es diferente de 5? -> {NumeroA != NumeroB}") 

# ==========================================
# Operadores Lógicos (and, or, not)
# ==========================================

print("\n-------------\n")

# Podemos combinar booleanos para tomar decisiones más complejas:

# 'and' (Y): Exige que TODAS las condiciones sean verdaderas
print(f"True and True -> {True and True}")
print(f"True and False -> {True and False}")

# 'or' (O): Es más relajado. Con que UNA sea verdadera, todo es verdadero
print(f"True or False -> {True or False}")
print(f"False or False -> {False or False}")

# 'not' (NO): Simplemente invierte el valor al opuesto
print(f"Lo contrario de True (not True) es -> {not True}")

# ==========================================
# Cambio de tipo de valor (Type Casting a bool)
# ==========================================

print("\n-------------\n")

# En Python, casi cualquier tipo de dato puede convertirse en booleano.
# A esto se le conoce como "Truthiness" (Veracidad).
# La regla general es: si está vacío o es cero, es False. Si tiene "algo", es True.

# 1. Números a Booleanos
# El número 0 es SIEMPRE False. Cualquier otro número (positivo o negativo) es True.
print(f"El número 1 convertido a bool es: {bool(1)}")
print(f"El número 0 convertido a bool es: {bool(0)}")

# 2. Texto a Booleanos
# Un texto completamente vacío "" es False.
print(f"Un texto vacío convertido a bool es: {bool('')}")

# Un texto con cualquier carácter (¡incluso un solo espacio en blanco!) es True.
print(f"Un texto con contenido convertido a bool es: {bool('Hola clase')}")