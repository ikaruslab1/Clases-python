# ==========================================
# Clase: Sesión 6 - Ciclos e Iteraciones
# Tema: Función incorporada range()
# Autor: Prof. Adrián Torres
# ==========================================

# La función range() genera una secuencia de números inmutables. 
# Es la herramienta definitiva para automatizar repeticiones cuando 
# sabemos EXACTAMENTE cuántas veces queremos iterar.

print("")

# ==========================================
# 1. range(fin) - Un solo parámetro
# ==========================================
print("--- 1. Generación Básica ---")

# Si le pasamos un solo número, range() empieza en 0 y termina 
# un número ANTES del límite indicado (igual que el Slicing).

LoteDePruebas: int = 3
print(f"Ejecutando {LoteDePruebas} pruebas de unidad:")

for i in range(LoteDePruebas):
    print(f"Ejecutando prueba número: {i}")

print("\n-------------\n")

# ==========================================
# 2. range(inicio, fin) - Dos parámetros
# ==========================================
print("--- 2. Rango con Inicio y Fin ---")

# Podemos definir desde qué número arrancar explícitamente.

AnioInicio: int = 2024
AnioFin: int = 2027 # El 2027 NO se incluye

print("Proyección del plan de estudios:")
for anio in range(AnioInicio, AnioFin):
    print(f"Plan correspondiente al año: {anio}")

print("\n-------------\n")

# ==========================================
# 3. range(inicio, fin, paso) y las "Épocas" en IA
# ==========================================
print("--- 3. Control exacto e introducción a Machine Learning ---")

# El tercer parámetro nos indica los "saltos" o el paso entre números.
# Esto es vital para controlar entrenamientos de modelos de Inteligencia Artificial.

TotalEpocas: int = 100 # Número total de veces que el modelo verá los datos
FrecuenciaReporte: int = 20 # Queremos un reporte cada 20 épocas

print("Iniciando entrenamiento del modelo...")

# Iteramos del 0 al 100, pero saltando de 20 en 20
for epoch in range(0, TotalEpocas + 1, FrecuenciaReporte):
    # Simulamos el reporte de progreso de la red neuronal
    if epoch == 0:
        continue # Nos saltamos el reporte en la época 0
        
    print(f"Época [Epoch] {epoch}/{TotalEpocas} -> Calculando margen de error de la red...")

print("Entrenamiento del modelo finalizado con éxito.")

print("\n-------------")
print("Fin de la Sesión 6.")