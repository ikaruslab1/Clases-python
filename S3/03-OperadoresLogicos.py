# ==========================================
# Clase: Sesión 3 - Operadores
# Tema: Lógicos
# Autor: Prof. Adrián Torres
# ==========================================

# Los operadores lógicos se utilizan para evaluar múltiples condiciones y 
# siempre devuelven un valor booleano (True o False). 
# En Python son palabras reservadas: 'and', 'or', 'not'.

# Definimos algunas variables booleanas para los primeros ejemplos
es_estudiante = bool(input('Selecciona True o dejar vacio (False): '))
tiene_beca = bool(input('Selecciona True o dejar vacio (False): '))

print(f"\n--- Valores: es_estudiante = {es_estudiante}, tiene_beca = {tiene_beca} ---\n")
print("-------------\n")

# 1. Operador 'and' (Y lógico)
# Evalúa si AMBAS condiciones son verdaderas. Si una es falsa, todo es falso.
resultado_and = es_estudiante and tiene_beca
print("Operador 'and':")
print(f"es_estudiante ({es_estudiante}) 'y' tiene_beca ({tiene_beca}) : {resultado_and}")

print(""" \n
      Valores esperados:
      True and True = True     <---- Único caso posible donde será true es cuando los dos son true
      True and False = False
      False and False = False
      """)

print("\n-------------\n")

# 2. Operador 'or' (O lógico)
# Evalúa si AL MENOS UNA de las condiciones es verdadera.
resultado_or = es_estudiante or tiene_beca
print("Operador 'or': ")
print(f"es_estudiante ({es_estudiante}) 'o' tiene_beca ({tiene_beca}): {resultado_or}")

print(""" \n
      Valores esperados:
      True and True = True
      True and False = True
      False and False = False  <---- Único caso posible donde será False es cuando existe al menos un False
      """)

print("\n-------------\n")

# 3. Operador 'not' (NO lógico / Negación)
# Invierte el valor de verdad. Lo que es True se vuelve False, y viceversa.
resultado_not_Uno = not es_estudiante
resultado_not_Dos = not tiene_beca
print ("Operador 'not':")
print(f"'No es' es_estudiante ({es_estudiante}): {resultado_not_Uno}")
print(f"'No es' tiene_beca ({tiene_beca}): {resultado_not_Dos}")

print(""" \n
      Valores esperados:
      True = False
      False = True
      """)

print("\n-------------\n")

# =============================================================================
# Ejemplo práctico combinando operadores relacionales (comparación) y lógicos
# =============================================================================
print("--- Ejemplo con expresiones de comparación ---")
print("\n-------------\n")

edad_usuario = 22
promedio_calificaciones = 8.5

# Supongamos que para un apoyo necesitamos que sea mayor de edad (>= 18) 
# Y que tenga un promedio mayor a 8.0
aplica_apoyo = (edad_usuario >= 18) and (promedio_calificaciones > 8.0)

print(f"Datos del usuario: Edad = {edad_usuario}, Promedio = {promedio_calificaciones}")
print(f"¿Aplica para el apoyo?: {aplica_apoyo}")

print("\n-------------")
print("Fin de la Sesión 3.")