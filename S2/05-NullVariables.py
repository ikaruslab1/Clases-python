# ==========================================
# Clase: Sesión 2 - Tipos de datos
# Tema: El valor Nulo (None) en Python
# Autor: Prof. Adrián Torres
# ==========================================

# 'NoneType' es un tipo de dato que tiene un único valor posible: None.
# 'None' en Python significa literalmente "nada", "vacío" o "ausencia de valor".

print("")

# Declaración de una variable nula.
# ¡Ojo!: Se escribe con la 'N' mayúscula.
# Se usa mucho cuando creamos una variable pero aún no sabemos qué dato va a contener.
DatoDesconocido = None

print(f"El valor de la variable es: {DatoDesconocido}")
print(f"El tipo de dato es: {type(DatoDesconocido).__name__}")

print("\n-------------\n")

# Aclaración crucial para los alumnos:
# ¡None NO es lo mismo que cero, ni lo mismo que un texto vacío, ni lo mismo que False!
# Cero es un número. "" es un texto. False es un booleano. None es la ausencia absoluta.

print(f"¿None es igual a 0? -> {None == 0}")
print(f"¿None es igual a un texto vacío ''? -> {None == ''}")
print(f"¿None es igual a False? -> {None == False}")

# La forma correcta y profesional de verificar si una variable es None 
# no es usar '==', sino la palabra reservada 'is' (identidad).
print(f"¿La variable es verdaderamente nula? -> {DatoDesconocido is None}")


print("\n-------------")
print("Fin de la Sesión 2.")