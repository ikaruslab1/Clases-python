# ==========================================
# Clase: Sesión 3 - Operadores
# Tema: Lógicos
# Autor: Prof. Adrián Torres
# ==========================================

# Los operadores lógicos se utilizan para evaluar múltiples condiciones y 
# siempre devuelven un valor booleano (True o False). 
# En Python son palabras reservadas: 'and', 'or', 'not'.

# Definimos algunas variables booleanas para los primeros ejemplos
es_estudiante = True
tiene_beca = False

print(f"--- Valores: es_estudiante = {es_estudiante}, tiene_beca = {tiene_beca} ---\n")

# 1. Operador 'and' (Y lógico)
# Evalúa si AMBAS condiciones son verdaderas. Si una es falsa, todo es falso.
resultado_and = es_estudiante and tiene_beca
print(f"Operador 'and' (es_estudiante AND tiene_beca): {resultado_and}")

# 2. Operador 'or' (O lógico)
# Evalúa si AL MENOS UNA de las condiciones es verdadera.
resultado_or = es_estudiante or tiene_beca
print(f"Operador 'or' (es_estudiante OR tiene_beca): {resultado_or}")

# 3. Operador 'not' (NO lógico / Negación)
# Invierte el valor de verdad. Lo que es True se vuelve False, y viceversa.
resultado_not = not es_estudiante
print(f"Operador 'not' (NOT es_estudiante): {resultado_not}")

# =============================================================================
# Ejemplo práctico combinando operadores relacionales (comparación) y lógicos
# =============================================================================
print("\n--- Ejemplo con expresiones de comparación ---")

edad_usuario = 22
promedio_calificaciones = 0.5

# Supongamos que para un apoyo necesitamos que sea mayor de edad (>= 18) 
# Y que tenga un promedio mayor a 8.0
aplica_apoyo = (edad_usuario >= 18) and (promedio_calificaciones > 8.0)

print(f"Datos del usuario: Edad = {edad_usuario}, Promedio = {promedio_calificaciones}")
print(f"¿Aplica para el apoyo?: {aplica_apoyo}")