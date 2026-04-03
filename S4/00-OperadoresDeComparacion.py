# ==========================================
# Clase: Sesión 4 - Operadores Relacionales
# Tema: Operadores de comparación (==, !=, >, < y el mito de ===)
# Autor: Prof. Adrián Torres
# ==========================================

# Los operadores de comparación (o relacionales) se utilizan para 
# comparar dos valores. El resultado de esta comparación siempre 
# será un valor booleano: True (Verdadero) o False (Falso).

print("")



# ==========================================
# 1. Operadores de Igualdad (==) y Desigualdad (!=)
# ==========================================

# '==' verifica si dos valores son IGUALES.
# '!=' verifica si dos valores son DIFERENTES.
# ¡Importante! No confundir '==' (comparación) con '=' (asignación).

PasswordIngresado: str = "python123"
PasswordCorrecto: str = "python123"

print("--- Evaluando Igualdad y Desigualdad ---")

if PasswordIngresado == PasswordCorrecto:
    print("Operador '==': Las contraseñas coinciden. Acceso concedido.")

IntentosFallidos: int = 3
LimiteIntentos: int = 5

if IntentosFallidos != LimiteIntentos:
    print("Operador '!=': Aún tienes intentos disponibles. Sigue intentando.")

print("\n-------------\n")



# ==========================================
# 2. Operadores de Magnitud (>, <, >=, <=)
# ==========================================

# Estos operadores evalúan qué valor es mayor o menor.
# >  Mayor que
# <  Menor que
# >= Mayor o igual que
# <= Menor o igual que

TemperaturaActual: float = 25.5
TemperaturaMaxima: float = 30.0
PuntoCongelacion: float = 0.0

print("--- Evaluando Magnitudes de Temperatura ---")

if TemperaturaActual < TemperaturaMaxima:
    print("Operador '<': La temperatura está por debajo del límite máximo.")

if TemperaturaActual >= PuntoCongelacion:
    print("Operador '>=': La temperatura es mayor o igual a cero. No hay riesgo de congelación.")

print("\n-------------\n")



# ==========================================
# 3. El mito del operador '===' en Python
# ==========================================

# Si vienes de lenguajes como JavaScript o PHP, estarás acostumbrado 
# a usar '===' (igualdad estricta) para comparar valor Y tipo de dato.
# 
# EN PYTHON, EL OPERADOR '===' NO EXISTE. Si lo escribes, 
# Python arrojará un error de sintaxis (SyntaxError).
# 
# ¿Por qué no existe? Porque en Python, el operador '==' ya es estricto 
# con los tipos de datos en la mayoría de los casos. Por ejemplo, 
# un número entero y un texto NUNCA serán iguales.

NumeroTexto: str = "5"
NumeroEntero: int = 5

print("--- Aclarando la ausencia de '===' ---")

# Esto evaluará a False directamente. Python no convierte automáticamente 
# el "5" en un número para hacerlos coincidir (como sí hace JavaScript con ==).
if NumeroTexto == NumeroEntero:
    print("Son iguales.")
else:
    print("Operador '==': Python sabe que un 'str' y un 'int' son diferentes. ¡No necesitamos '==='!")

# REPASO: Si lo que buscas es saber si dos cosas son exactamente 
# el MISMO objeto en la memoria del sistema, usamos el operador 'is', 
# el cual estudiamos en la sesión anterior.