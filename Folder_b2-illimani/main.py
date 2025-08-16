#!/usr/bin/python3
# Illimani, es el nombre de una método de cifrado por selección de elementos en posiciones pares e impares de un texto introducido. Es decir, se toman todos los caracteres que se encuentran en posiciones impares, y así se conforma la primera parte del mensaje cifrado, y luego se toman los caracteres que se encuentran en las posiciones pares, conformando así la segunda parte del mensaje, luego se juntan ambas partes, y ya tienes el mensaje CIFRADO.

# La entrada tiene una cadena de caracteres de hasta 1000 letras, todas son solamente letras, no hay signos de puntación ni acentos ni caracteres especiales, el único caracter especial que se admite es el espacio.
# Hola Mundo

# Leer la entrada completa (incluyendo espacios)
text = input()

# Separar caracteres en posiciones impares (índices 0, 2, 4, ...)
imp=""
par=""
# Recorrer cada carácter con su índice
for x, char in enumerate(text):
    if x % 2 == 0:  # Posición impar (índice par)
        imp += char
    else:  # Posición par (índice impar)
        par += char

print(imp + par)
