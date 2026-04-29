# ==========================================
# Clase: Sesión 5 - Estructuras de Datos Secuenciales
# Tema: Indexación y Slicing (Rebanado)
# Autor: Prof. Adrián Torres
# ==========================================

# Cuando trabajamos con grandes volúmenes de datos, casi nunca queremos 
# usar toda la lista al mismo tiempo. Necesitamos extraer datos específicos.

print("")

DatasetAlumnos: list[str] = ["Ana", "Beto", "Carlos", "Diana", "Elena", "Fernando"]

# ==========================================
# 1. Indexación (Extraer un solo elemento)
# ==========================================
print("--- Indexación Básica y Negativa ---")

# Indexación Positiva: De izquierda a derecha (empieza en 0)
PrimerAlumno = DatasetAlumnos[0]
print(f"El primer alumno (índice 0) es: {PrimerAlumno}")

# Indexación Negativa: De derecha a izquierda (empieza en -1)
# ¡Truco de Python! Si quieres el último elemento sin importar qué tan 
# larga sea la lista, usa el índice -1.
UltimoAlumno = DatasetAlumnos[-1]
PenultimoAlumno = DatasetAlumnos[-2]
print(f"El último alumno (índice -1) es: {UltimoAlumno}")
print(f"El penúltimo alumno (índice -2) es: {PenultimoAlumno}")

print("\n-------------\n")

# ==========================================
# 2. Slicing o Rebanado (Extraer subconjuntos)
# ==========================================
# La sintaxis del slicing es: lista[inicio : fin : paso]
# - inicio: donde empezamos (se incluye)
# - fin: donde terminamos (NO se incluye)
# - paso: de cuánto en cuánto saltamos (opcional)

print("--- Slicing (Rebanado) ---")
print(f"Lista completa: {DatasetAlumnos}")

# Extraer los primeros 3 elementos (índices 0, 1 y 2. El 3 no se incluye)
PrimerosTres = DatasetAlumnos[0:3] 
print(f"Primeros tres alumnos [0:3]: {PrimerosTres}")

# Si omites el inicio, Python asume que es desde el principio
MismoResultado = DatasetAlumnos[:3]
print(f"Atajo para los primeros tres [:3]: {MismoResultado}")

# Extraer desde el índice 3 hasta el final
DesdeElTercero = DatasetAlumnos[3:]
print(f"Desde el índice 3 al final [3:]: {DesdeElTercero}")

# Extraer con saltos (Paso)
# Esto es muy útil para separar datos de entrenamiento y prueba en Machine Learning
DeDosEnDos = DatasetAlumnos[0:6:2] # O simplemente DatasetAlumnos[::2]
print(f"Alumnos de dos en dos [0:6:2]: {DeDosEnDos}")

# Un truco avanzado: Invertir una lista completa usando un paso negativo
ListaInvertida = DatasetAlumnos[::-1]
print(f"Lista invertida [::-1]: {ListaInvertida}")