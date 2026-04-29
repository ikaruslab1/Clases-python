# ==========================================
# Clase: Sesión 5 - Estructuras de Datos Secuenciales
# Tema: Tuplas (tuple) y su Inmutabilidad
# Autor: Prof. Adrián Torres
# ==========================================

# Las tuplas son primas hermanas de las listas. Sirven para almacenar 
# múltiples valores, pero se definen con paréntesis ( ) en lugar de corchetes [ ].

print("")

# ==========================================
# 1. Declaración de Tuplas
# ==========================================

# Son ideales para agrupar datos que conceptualmente van juntos y no deben separarse.
# Por ejemplo, un valor de color RGB en diseño gráfico o coordenadas geográficas.

ColorPrimarioRGB: tuple[int, int, int] = (255, 0, 0) # Representa el color Rojo puro
CoordenadasFES: tuple[float, float] = (19.4735, -99.2462)

print("--- Explorando Tuplas ---")
print(f"El color RGB es: {ColorPrimarioRGB}")
print(f"Tipo de dato: {type(ColorPrimarioRGB).__name__}")

# La función len() también funciona perfectamente con las tuplas
print(f"El color RGB tiene {len(ColorPrimarioRGB)} canales (R, G, B).")

print("\n-------------\n")

# ==========================================
# 2. Inmutabilidad (No se pueden cambiar)
# ==========================================

# A diferencia de las listas, las tuplas son INMUTABLES. 
# Una vez creadas, NO puedes alterar, borrar ni añadir elementos. 
# Son como datos grabados en piedra. 

print("--- Inmutabilidad ---")
ConfiguracionServidor: tuple[str, int] = ("localhost", 8080)
print(f"Configuración inicial: {ConfiguracionServidor}")

# Si intentáramos hacer esto:
# ConfiguracionServidor[1] = 9000
# Python nos arrojaría un 'TypeError', deteniendo el programa, porque 
# las tuplas no soportan la asignación de elementos.

print("¿Por qué usar tuplas si no se pueden modificar?")
print("1. Por seguridad: Proteges datos que son críticos (como contraseñas o configuraciones).")
print("2. Por rendimiento: Al ser fijas, Python las procesa un poco más rápido que las listas.")