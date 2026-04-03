# ==========================================
# Clase: Sesión 4 - Control de Flujo
# Tema: Condicionales Anidadas y Operador Ternario
# Autor: Prof. Adrián Torres
# ==========================================

print("")



# ==========================================
# 1. Condicionales Anidadas
# ==========================================
# Podemos colocar un 'if' dentro de otro 'if'. A esto se le llama anidación.
# Es importante respetar la indentación para no perdernos.

UsuarioRegistrado: bool = True
RolUsuario: str = "Profesor"

print("--- Verificando permisos del portal ---")

if UsuarioRegistrado:
    print("El usuario existe en la base de datos.")
    
    # Este 'if' está dentro del primer 'if'
    if RolUsuario == "Profesor":
        print("-> Tienes permisos para modificar calificaciones y planes de estudio.")
    elif RolUsuario == "Alumno":
        print("-> Tienes permisos de solo lectura para ver tus materias.")
    else:
        print("-> Rol no reconocido. Contacta a soporte técnico.")
else:
    print("Debes iniciar sesión para acceder al portal.")

print("\n-------------\n")



# ==========================================
# 2. Operador Ternario (If de una sola línea)
# ==========================================
# Es una forma compacta de escribir un if-else cuando queremos 
# asignar un valor a una variable de forma rápida.

# Estructura: 
# [Valor si es True] if [Condición] else [Valor si es False]

ModeloEntrenado: bool = True

# En lugar de escribir 4 líneas de código, lo resolvemos en 1:
EstadoDelModelo: str = "Listo para predicciones" if ModeloEntrenado  else "Requiere más datos"

print(f"Estado del modelo de IA: {EstadoDelModelo}")


print("\n-------------")
print("Fin de la Sesión 4.")