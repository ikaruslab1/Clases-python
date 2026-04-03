# ==========================================
# Clase: Sesión 2 - Tipos de datos
# Tema: Texto (str) en Python
# Autor: Prof. Adrián Torres
# ==========================================

# 'str' hace referencia a la palabra String ("cadena" en inglés).
# Es el tipo de dato que usamos para almacenar secuencias de caracteres (texto).

# Imprime una línea en blanco en la consola para dar espacio y limpieza visual
print("") 

# Declaración de una variable de texto.
# Usar ': str' es una "Pista de Tipo" (Type Hinting). En Python no es obligatorio,
# pero es una buena práctica profesional para ser estrictos y ayudar al editor de código.
VariableDeTexto: str = "variable de texto"

print("\n-------------\n")

# ==========================================
# Tipos de comillas para las variables de texto
# ==========================================

# Python es flexible y permite usar diferentes tipos de comillas para definir un texto.
# Comillas dobles y simples funcionan exactamente igual para una sola línea de texto.
StrComillasDobles = "Un texto con comillas dobles"
StrComillasSimples = 'Un texto con comillas simples'

# Las comillas triples también funcionan, pero tienen un superpoder...
StrComillasTriplesSimples = '''Un texto con comillas triples simples'''
StrComillasTriplesDobles = """Un texto con comillas triples dobles"""

# ...el superpoder de las comillas triples es que respetan los saltos de línea (Enter).
# Son ideales para párrafos o textos largos.
# \n cumple la misma función de escapar una línea
TextoMultilinea = """Este es un texto
que puede saltar de línea
fácilmente."""

# Imprimimos todas las variables creadas para ver sus resultados en consola
print(StrComillasDobles)
print(StrComillasSimples)
print(StrComillasTriplesSimples)
print(StrComillasTriplesDobles)
print(TextoMultilinea)

print("\n-------------\n")

# f-strings (Cadenas con formato): Poner una 'f' antes de las comillas nos permite
# inyectar variables directamente dentro del texto usando llaves { }.
print(f"Este es un texto formateado para imprimir una {VariableDeTexto}")

# ¿Para qué sirve tener diferentes comillas? 
# Si usas comillas simples por fuera, puedes imprimir comillas dobles por dentro 
# (y viceversa) sin que Python marque un error de sintaxis.
print('Este es un texto "Literal"')

# ==========================================
# Cambio de tipo de valor (Type Casting)
# ==========================================

# Usamos comillas triples aquí solo para imprimir un separador visual de varias líneas
print("\n-------------\n")

# 1. Asignamos un número entero (int) a la variable
DeNumeroATexto = 10
print(f"{DeNumeroATexto} es un número" )

# La función type() nos revela que la variable es de la clase 'int' (entero)
print(type(DeNumeroATexto))

# 2. Convertimos (casteamos) el número 10 a texto usando la función str()
DeNumeroATexto = str(10)
print(f"Ahora {DeNumeroATexto} es un texto" )

# Comprobamos que el tipo cambió. Ahora la función type() mostrará la clase 'str'
print(f'{DeNumeroATexto} es un {type(DeNumeroATexto).__name__}')



