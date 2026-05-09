# ==========================================
# Clase: Sesión 6 - Ciclos e Iteraciones
# Tema: Ciclo for aplicado a secuencias de datos
# Autor: Prof. Adrián Torres
# ==========================================

# A diferencia del 'while', el ciclo 'for' (para cada) en Python está diseñado 
# específicamente para iterar (recorrer) sobre elementos de una secuencia, 
# como las listas, tuplas o cadenas de texto que vimos en la sesión anterior.

print("")

# ==========================================
# 1. Iterando sobre una Lista
# ==========================================
print("--- 1. Recorriendo Listas ---")

# Declaramos nuestra lista con Type Hinting
ModelosIA: list[str] = ["Regresión Lineal", "Redes Neuronales", "Árboles de Decisión"]

# Leemos esto como: "Para cada 'modelo' dentro de la lista 'ModelosIA'..."
# La variable 'modelo' toma el valor de un elemento diferente en cada iteración.
for modelo in ModelosIA:
    print(f"Analizando el algoritmo de: {modelo}")

print(f"Total de modelos iterados: {len(ModelosIA)}")

print("\n-------------\n")

# ==========================================
# 2. Iterando sobre una Cadena de Texto (str)
# ==========================================
print("--- 2. Recorriendo Cadenas de Texto ---")

# Los textos también son secuencias. El for recorrerá letra por letra.
NombreDataset: str = "Datos.csv"
VocalesEncontradas: int = 0

print(f"Inspeccionando el texto '{NombreDataset}':")

for caracter in NombreDataset:
    # Usamos un if para contar cuántas 'a', 'e', 'i', 'o', 'u' existen
    if caracter.lower() in ["a", "e", "i", "o", "u"]:
        VocalesEncontradas += 1
        print(f"-> Vocal encontrada: {caracter}")

print(f"El texto contiene {VocalesEncontradas} vocales.")

print("\n-------------")
print("Fin del Tema 2.")