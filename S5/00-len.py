# ==========================================
# Clase: Sesión 5 - Estructuras de Datos Secuenciales
# Tema: Función incorporada len() y sus aplicaciones
# Autor: Prof. Adrián Torres
# ==========================================

# La función len() (abreviatura de "length" o longitud en inglés) es una
# herramienta fundamental en Python. Nos permite conocer el tamaño exacto 
# (cantidad de elementos) de cualquier estructura secuencial.

print("")

# ==========================================
# 1. len() en Cadenas de Texto (str)
# ==========================================
print("--- 1. Midiendo Textos ---")
# Una cadena de texto también es una secuencia (de caracteres).
# len() cuenta cada carácter, incluyendo espacios en blanco y signos de puntuación.

NombreArchivo: str = "dataset_entrenamiento_ia.csv"
LongitudTexto = len(NombreArchivo)

print(f"El archivo '{NombreArchivo}' tiene {LongitudTexto} caracteres.")

# Aplicación práctica: Validaciones de seguridad o formato
PasswordInput: str = "admin123"
if len(PasswordInput) >= 8:
    print("Validación: La longitud de la contraseña es segura.")
else:
    print("Error: La contraseña es muy corta.")

print("\n-------------\n")

# ==========================================
# 2. len() en Listas y Tuplas (Vectores y Matrices)
# ==========================================
print("--- 2. Midiendo Listas y Tuplas ---")
# En listas y tuplas, len() no cuenta caracteres, sino los elementos individuales
# separados por comas, sin importar de qué tipo de dato sean.

# Ejemplo de Diseño: Una paleta cromática con 5 colores hexadecimales
PaletaColores: list[str] = ["#FF5733", "#33FF57", "#3357FF", "#F033FF", "#33FFF0"]
print(f"La paleta de diseño contiene {len(PaletaColores)} colores.")

# Ejemplo de IA: Una tupla representando las dimensiones de una imagen (Ancho, Alto, Canales)
DimensionesImagen: tuple[int, int, int] = (1920, 1080, 3)
print(f"La tupla de dimensiones tiene {len(DimensionesImagen)} valores.")

print("\n-------------\n")

# ==========================================
# 3. Aplicación Crítica: Evitar Errores de Índice (IndexError)
# ==========================================
print("--- 3. Prevención de IndexError ---")
# Un error clásico al empezar a programar es intentar extraer un dato en una
# posición que no existe. La función len() es nuestra brújula.

CapaNeuronal: list[float] = [0.5, -0.2, 0.8]
TotalNeuronas = len(CapaNeuronal)

print(f"Tenemos {TotalNeuronas} pesos sinápticos en esta capa.")

# ¡CUIDADO! El número total de elementos NO es el índice máximo.
# Como en programación empezamos a contar desde el 0, el índice máximo 
# para extraer el último elemento de cualquier lista siempre es: len() - 1

IndiceMaximo = TotalNeuronas - 1
print(f"El último elemento está en el índice {IndiceMaximo} y su valor es: {CapaNeuronal[IndiceMaximo]}")

print("\n-------------\n")

# ==========================================
# 4. Aplicación Crítica: Comparación de Dimensiones
# ==========================================
print("--- 4. Validación de Datos (Machine Learning) ---")
# Antes de sumar, multiplicar o procesar dos vectores en sistemas de IA,
# es una regla matemática estricta verificar que tengan la misma dimensión (longitud).

VectorEntradaX: list[int] = [10, 20, 30, 40]
VectorEntradaY: list[int] = [5, 15, 25] # A este vector le falta un dato

print(f"Vector X (tamaño {len(VectorEntradaX)}): {VectorEntradaX}")
print(f"Vector Y (tamaño {len(VectorEntradaY)}): {VectorEntradaY}")

# Usamos if-else junto con len() para proteger nuestro programa de crasheos matemáticos
if len(VectorEntradaX) == len(VectorEntradaY):
    print("Éxito: Los vectores tienen la misma dimensión. Listos para procesar.")
else:
    print("Error Crítico: Incompatibilidad de dimensiones. Revisa la limpieza de tu dataset.")

print("\n-------------")
print("Fin de la Sesión 5.")