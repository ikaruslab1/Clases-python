# ==========================================
# Archivo: EjerciciosVariables.py
# Autor: Prof. Adrián Torres
# Tema: Variables y Tipos de Datos Primitivos
# ==========================================

print("Iniciando ejercicios...\n")

# ==========================================
# EJERCICIO 1: El Perfil del Estudiante
# ==========================================
print("--- Ejercicio 1 ---")
# Instrucción: Declara las siguientes variables usando Pistas de Tipo (Type Hinting).
# Elige el tipo de dato primitivo adecuado (str, int, float, bool, NoneType).
# Después imprime por pantalla la variable y un texto referente

#Ejemplo:
EjemploTipoDeDato: any = "Ejemplo"
print(f'1.0 - Este es un {EjemploTipoDeDato}')

# 1. Tu nombre completo
# Escribe tu código aquí:


# 2. Tus años cumplidos
# Escribe tu código aquí:


# 3. Un promedio ficticio con decimales (ej. 9.5)
# Escribe tu código aquí:


# 4. Un valor lógico que indique que actualmente eres alumno
# Escribe tu código aquí:


# 5. Una variable para un segundo apellido, pero déjala sin valor asignado (nula)
# Escribe tu código aquí:





# ==========================================
# EJERCICIO 2: ¿Quién es quién?
# ==========================================
print("\n--- Ejercicio 2 ---")
# Instrucción: Escribe como comentario al lado de cada variable qué tipo de dato es.
# Opciones: str, int, float, bool, NoneType
# Después imprime por pantalla que tipo de dato es con le método type

dato_0 = any     # Respuesta: Any
print(f"2.0 - '{type(dato_0)}' es un tipo de dato any")

dato_a = "2024"  # Respuesta: 
dato_b = 2024    # Respuesta: 
dato_c = 2024.0  # Respuesta: 
dato_d = True    # Respuesta: 
dato_e = "False" # Respuesta: 
dato_f = None    # Respuesta: 




# ==========================================
# EJERCICIO 3: El Laboratorio de Transformación (Casting)
# ==========================================
print("\n--- Ejercicio 3 ---")
# Instrucción: Realiza las conversiones solicitadas. Imprime el valor resultante
# y su nuevo tipo de dato usando type() y f-strings.

# 0. Ejemplo
Ejemplo_null = any
# Escribe tu código aquí:
print(f'{type(Ejemplo_null)}')
Ejemplo_null = None
print(f'{type(Ejemplo_null)}')

# 1. Convierte el siguiente texto a un número entero
precio_texto = "450"
# Escribe tu código aquí:



# 2. Convierte el siguiente número a un número entero (observa qué pasa con los decimales)
estatura = 1.75
# Escribe tu código aquí:



# 3. Convierte el siguiente número a un valor booleano
es_adulto = 1
# Escribe tu código aquí:



# 4. Convierte el siguiente valor nulo a un formato de texto (str)
vacio = None
# Escribe tu código aquí:



# ==========================================
# EJERCICIO 4: Cacería de Errores (Sintaxis)
# ==========================================
print("\n--- Ejercicio 4 ---")
# Instrucción: El siguiente código está comentado porque tiene errores.
# Quita el símbolo '#' de las variables, encuentra el error y corrígelo
# para que Python pueda ejecutarlo sin problemas.

# A) Intentar guardar un texto multilínea:
# nota = "Este es un recordatorio
# importante para la clase"

# B) Declaración de tipo (Type Hinting) ilógica:
# poblacion: int = "8000"

# C) Error de mayúsculas en booleanos:
# es_graduado: bool = true




# ==========================================
# EJERCICIO 5: Formateo de Mensajes (f-strings)
# ==========================================
print("\n--- Ejercicio 5 ---")
# Instrucción: Declara las tres variables solicitadas e imprime el mensaje
# exacto usando una sola f-string.

# 1. Declara: materia, profesor y sesion
# Escribe tu código aquí:



# 2. Imprime: "Bienvenidos a la clase de [materia] con el [profesor]. Estamos en la [sesion]."
# Sustituye los corchetes por las variables usando f-strings.
# Escribe tu código aquí:


print("\n¡Ejercicios finalizados!")