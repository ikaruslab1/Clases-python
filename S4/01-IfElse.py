# ==========================================
# Clase: Sesión 4 - Control de Flujo
# Tema: Sentencias condicionales (if, else, elif)
# Autor: Prof. Adrián Torres
# ==========================================

# El control de flujo nos permite que el programa tome decisiones.
# Dependiendo de si una condición es Verdadera (True) o Falsa (False), 
# el código ejecutará un bloque de instrucciones u otro.

print("")

# ==========================================
# 1. La sentencia 'if' (Si...)
# ==========================================

# Declaramos una variable numérica para evaluar
CalificacionAlumno: float = 8.5

# Si la condición (CalificacionAlumno >= 8.0) se cumple, ejecutamos el código de abajo.
# NOTA: En Python, el espacio en blanco antes del print se llama "Indentación".
# Es obligatorio para indicarle a Python qué código pertenece dentro del 'if'.
if CalificacionAlumno >= 8.0:
    print(f"¡Felicidades! Aprobaste la materia con {CalificacionAlumno}.")

# Se puede emplear la palara reservada 'is', para saber si la variable que se está
# comparando es exáctamente igual (lo mismo que un comparador estricto ==)

if CalificacionAlumno is 8.5:
    print(f"Se ha confirmado que su calificación es: {CalificacionAlumno}")

# Este código no se imprimir ya que el resultado es false, por lo tanto no se ejecuta

if CalificacionAlumno is 8:
    print(f"Se ha confirmado que su calificación es: {CalificacionAlumno}")

# Podemos leerlo de la siguiente forma:
# ¿Es CalificacionAlumno exáctamente igual a 8?
# No, tanto en valor como en tipo de dato (int != float)
# Por lo tanto no se ejecuta el print

print("\n-------------\n")



# ==========================================
# 2. La sentencia 'else' (Si no...)
# ==========================================

# ¿Qué pasa si la condición es falsa? Usamos 'else' para dar una alternativa.
EdadUsuario: int = 16

print(f"Verificando acceso para un usuario de {EdadUsuario} años...")

if EdadUsuario >= 18:
    print("Acceso permitido al sistema.")
else:
    print("Acceso denegado. Eres menor de edad.")

print("\n-------------\n")



# ==========================================
# 3. La sentencia 'elif' (Si no, si...)
# ==========================================

# 'elif' es una abreviación de "else if". Nos sirve para evaluar múltiples 
# condiciones en cadena. En cuanto una se cumple, el resto se ignora.

PuntajeExamen: int = 75

print(f"Tu puntaje es {PuntajeExamen}.")

if PuntajeExamen >= 90:
    print("Calificación: Excelente (A)")
elif PuntajeExamen >= 80:
    print("Calificación: Muy Bien (B)")
elif PuntajeExamen >= 70:
    print("Calificación: Bien (C) - Aprobado")
else:
    # Si ninguna de las condiciones de arriba se cumple, cae en el 'else'
    print("Calificación: Insuficiente (NA) - Necesitas recursar")