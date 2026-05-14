# ==========================================
# Clase: Sesión 7 - Estructuras de Datos de Mapeo
# Tema: Conjuntos o Sets y el manejo de valores únicos
# Autor: Prof. Adrián Torres
# ==========================================

# Un conjunto es una colección desordenada de elementos únicos.
# Son extremadamente útiles cuando necesitamos limpiar bases de datos
# eliminando registros duplicados de forma automática.

print("")
print("--- 1. Declaración de Conjuntos ---")

# Los conjuntos también emplean llaves pero no tienen estructura de clave-valor
# solo contienen elementos individuales separados por comas.
CorreosAlumnos = {"ana@mail.com", "beto@mail.com", "carlos@mail.com"}

print(f"Correos registrados: {CorreosAlumnos}")
print(f"Tipo de dato: {type(CorreosAlumnos).__name__}")

print("\n-------------------\n")

print("--- 2. Manejo de valores únicos ---")

# Simulamos una lista de asistencia donde algunos alumnos se registraron dos veces.
AsistenciaConDuplicados = ["ana", "beto", "ana", "diana", "beto", "carlos"]
print(f"Lista con duplicados: {AsistenciaConDuplicados}")

# Al convertir la lista en un conjunto Python elimina los duplicados instantáneamente.
AsistenciaLimpia = set(AsistenciaConDuplicados)
print(f"Asistencia limpia usando set: {AsistenciaLimpia}")

print("\n-------------------\n")

print("--- 3. Agregar y eliminar elementos en conjuntos ---")

# Usamos add para agregar un solo elemento nuevo.
CorreosAlumnos.add("elena@mail.com")
print(f"Conjunto tras agregar un correo: {CorreosAlumnos}")

# Usamos remove para quitar un elemento específico.
CorreosAlumnos.remove("beto@mail.com")
print(f"Conjunto tras eliminar un correo: {CorreosAlumnos}")