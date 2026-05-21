# ==========================================
# Clase: Sesión 8 - Funciones y Modularidad
# Tema: Parámetros posicionales, argumentos nombrados y valores por defecto
# Autor: Prof. Adrián Torres
# ==========================================

# Las funciones son más poderosas cuando pueden recibir información del exterior
# para procesarla. A estas variables receptoras les llamamos "parámetros".

print("")
print("--- 1. Parámetros y Type Hinting ---")

# Al igual que con las variables, es una excelente práctica profesional
# usar Type Hinting para especificar qué tipo de dato espera recibir la función.
def saludar_alumno(nombre: str, carrera: str):
    print(f"Bienvenido/a {nombre}, mucho éxito en la carrera de {carrera}.")

# Al invocarla, debemos enviarle los "argumentos" exactamente en el mismo 
# orden en que se definieron los parámetros (Argumentos Posicionales).
saludar_alumno("Carlos", "Relaciones Internacionales")
saludar_alumno("Diana", "Actuaría")

print("\n-------------------\n")

print("--- 2. Argumentos Nombrados (Keyword arguments) ---")

# Si usamos el nombre exacto del parámetro al invocar la función, 
# el orden ya no importa. Esto hace el código extremadamente legible.
saludar_alumno(carrera="Derecho", nombre="Elena")

print("\n-------------------\n")

print("--- 3. Valores por Defecto ---")

# Podemos asignar un valor predeterminado a un parámetro desde la definición.
# Si el usuario no envía ese dato al llamar la función, Python usará el default.
# ¡Importante! Los parámetros con default siempre deben ir al final.

def configurar_modelo_ia(modelo: str, epocas: int = 100, learning_rate: float = 0.01):
    print(f"Configurando red '{modelo}':")
    print(f"-> Épocas de entrenamiento: {epocas}")
    print(f"-> Tasa de aprendizaje (LR): {learning_rate}")

print("Llamada 1: Enviando solo el parámetro obligatorio:")
configurar_modelo_ia("Transformer_v1")

print("\nLlamada 2: Sobrescribiendo los valores por defecto:")
# Modificamos las épocas, pero dejamos el LR por defecto usando argumentos nombrados
configurar_modelo_ia("ResNet_v2", epocas=500)