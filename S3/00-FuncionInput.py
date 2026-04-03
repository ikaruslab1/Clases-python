# ==========================================
# Clase: Sesión 2 - Tipos de datos
# Tema: Función incorporada type()
# Autor: Prof. Adrián Torres
# ==========================================

# 'input' es una función incorporada de python para que el usuario, a travéz
# de la interfaz de la terminal, pueda agregar manualmente un valor a una variable.
# La sintaxis consta de la función y los paréntesis donde estará el texto que teclé
# el usuario para ser asignado a la variable.

x = input()
print(f"Lo escrito en la variable 'x' fue: {x}")

"""
x = input()  <---- Declaramos la varibale, con un valor None por defecto, hasta que el usuario escriba algo
print(x)  <-- Una vez el usuario escriba algo y dé enter, este valor se imprimirá por pantalla
"""

print("\n-------------\n")

# Input es mucho más complejo de lo que parece, por defecto, lo que escriba el usuario
# será colocalo en la varibale como un string, vamos a comprobarlo: 

print(f"El tipo de dato de 'x'({x}) es {type(x).__name__}")
print("\n-------------\n")

# No importa si nosotros escribimos un número, este siempre será un str:

print(f"Es 'x'({x})  un número? {type(x).__name__ == int}")
print("\n-------------\n")

# Esto resulta en un error de lógica evidente, no podemos hacer operaciones matemáticas 
# con el comportamiento por defecto de input().
# Para hacer más estricto el comportamiento de la función input, es necesario agregar
# Type Hinting, de la siguiente forma:

y = int(input())
suma = y + y
print(f"El tipo de dato de 'y' es: {type(y).__name__}")
print(f"El resultado de la suma es: {suma}")

# Como puedes observar hasta el momento, el comportamiento de la terminal cambio
# Nos pide al principio un valor en la terminal, ejecuta el código corrrespindiente
# a la variable 'x' y nos pide ahora el valor para ejecuar la lógica de la variable
# y, esto se debe la función del código que se ejecuta en 'cascada'

# Más importante aún, la lógica la función input se hizo más compleja
# ahora solamente adminte números, no textos o dejar vacia la casilla

# Cuando aplicamos type hinting la función input, dependiendo del valor
# declarado, es el tipo de dato esperado, aquí te muestro el valor esperado
# de cada uno de los datos primitivos:

"""
int(input())   <---- Acepta: Número enteros, negativos y flotantes
str(input())   <---- Acepta: Cadenas de texto únicamente
bool(input)    <---- Acepta: Caulquier cosa escrita será True, dar enter sin escribir nada será False
float(input()) <---- Acepta: Número flotantes y enteros (no es recomendable emplear enteros)
any(input())   <---- Acepta: Este caso es interesante, los booleanos son una subclase de los número enteros
                             para entender por que pasa esto debes contestar lo siguiente:
                             ¿1 existe? -> Si, existe, por lo tanto es false
                             ¿'' existe? -> No, es un espacio vacio
                             La existencia o no existencia de algo es una propiedad de las cosas, por lo tanto todo valor
                             declarado es, ineheretemente, un booleano True.
"""
print("\n-------------\n")
# Ahora, una cosa interesante es que entre los paréntesis de la función
# input, podemos colocar un texto, que se mostrará al usuario,
# Esto simula una interfaz más humana:

z:str = str(input("Coloca un texto aquí: "))
print(f"El texto que escribiste fue: {z}")


# Como último tip, puedes emplear la función input simplemente como un 
# comando para terminar de forma elegante la interacción con la terminal, 
# si no está en la declaración de una variable, no guarda nada y simplemente 
# es un disparador:

print("\n-------------\n")
input("Presiona ENTER para terminar")
print("\n-------------\n")