# ==========================================
# Clase: Sesión 6 - Ciclos e Iteraciones
# Tema: Control de iteraciones con break y continue
# Autor: Prof. Adrián Torres
# ==========================================

# A veces necesitamos alterar el flujo normal de un ciclo desde adentro.
# Para esto existen dos palabras reservadas clave: 'break' y 'continue'.

print("")

# ==========================================
# 1. La sentencia 'break' (Romper)
# ==========================================
print("--- 1. Deteniendo el ciclo con break ---")

# 'break' termina el ciclo inmediatamente, sin importar si la condición 
# principal aún se cumple o si quedan elementos por iterar.

Servidores: list[str] = ["Activo", "Activo", "Caído", "Activo", "Activo"]
Posicion: int = 0

print("Buscando fallos en la red...")

for estado in Servidores:
    if estado == "Caído":
        print(f"¡Alerta crítica! Servidor caído encontrado en el índice {Posicion}.")
        print("Deteniendo la búsqueda para iniciar reparaciones de emergencia...")
        break  # El ciclo se destruye aquí, los siguientes servidores no se evalúan.
    
    print(f"Servidor en índice {Posicion} está en buen estado.")
    Posicion += 1

print("\n-------------\n")

# ==========================================
# 2. La sentencia 'continue' (Saltar)
# ==========================================
print("--- 2. Omitiendo iteraciones con continue ---")

# 'continue' NO destruye el ciclo. Solamente cancela la iteración ACTUAL
# y obliga al ciclo a saltar al siguiente elemento de la secuencia.

EdadesUsuarios: list[int] = [22, -5, 19, 0, 25]
UsuariosValidos: int = 0

print("Limpiando datos del sistema (Data Cleaning):")

for edad in EdadesUsuarios:
    # Si encontramos un dato basura (edad negativa o cero), nos lo saltamos
    if edad <= 0:
        print(f"Descartando dato erróneo ({edad}).")
        continue  # Salta inmediatamente al siguiente número en la lista
    
    # Este código solo se ejecuta si el continue no fue activado
    print(f"Procesando usuario válido de {edad} años.")
    UsuariosValidos += 1

print(f"Proceso finalizado. Total de usuarios registrados correctamente: {UsuariosValidos}")

print("\n-------------")
print("Fin del Tema 3.")