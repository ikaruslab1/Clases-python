# ==========================================
# Clase: Sesión 2 - Tipos de datos
# Tema: Función incorporada type()
# Autor: Prof. Adrián Torres
# ==========================================

# 'type' es una función incorporada de python para saber el tipo de valor
# que tenemos dentro de ella, la sintaxis es la declaración de la función
# y entre paréntesis el valor que queremos inspeccionar

x: str = "Dato 1"
type(x)
print(type(x))

"""
x: str          <--- Inicializamos la variable 'x' como una cadena de texto
type(x)         <--- Inspeccionamos el tipo de dato de la variable 'x' (esto no imprime nada por pantalla)
print(type(x))  <--- Opcionalmente, podemos imprimirlo por pantalla
"""

# Al ejecutar el código anterior, por pantalla vemos '<class 'str'>'
# Esto nos dice la categoria (class  o clase) y el nombre del dato (str)
print("\n-------------\n")
# Podemos ver de forma más clara el valor con el método de 
# la función incorporada type(), empleando la sintaxis; .__name__ al finaldsdf

y: bool = False
type(y).__name__
print(type(y).__name__)

# Ahora, el resultado es más limpio al acceder solamente al nombre del tipo de dato
# de la función type.