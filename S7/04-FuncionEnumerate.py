# ==========================================
# Clase: Sesión 7 - Estructuras de Datos de Mapeo
# Tema: Función enumerate para limpieza y procesamiento de datos
# Autor: Prof. Adrián Torres
# ==========================================

# La función enumerate resuelve un problema muy común ya que nos permite recorrer
# una secuencia y obtener simultáneamente la posición exacta o índice y el
# valor del elemento. Esto es una técnica crítica al procesar un dataset.

print("")

# Imaginemos un dataset pequeño extraído de un archivo de texto.
DatasetCrudo = ["Dato_A", "Dato_B", "Dato_Erroneo", "Dato_C", "Dato_Erroneo"]

print("--- Limpieza de datos con enumerate ---")

# Usamos enumerate envolviendo a nuestra lista en el ciclo for.
# Enumerate nos entregará dos variables en cada vuelta primero el índice numérico
# y después el valor almacenado en esa posición.
for Indice, Valor in enumerate(DatasetCrudo):
    
    # Evaluamos si encontramos un dato corrupto que necesita ser reemplazado.
    if Valor == "Dato_Erroneo":
        print(f"Alerta: Se encontró un error en la posición {Indice}. Corrigiendo el registro.")
        # Gracias a que tenemos el índice exacto podemos modificar la lista original.
        DatasetCrudo[Indice] = "Dato_Corregido"
    else:
        print(f"El registro en el índice {Indice} está correcto: {Valor}")

print("\n-------------------\n")

print(f"Dataset final procesado: {DatasetCrudo}")
print("\nFin de la Sesión 7.")