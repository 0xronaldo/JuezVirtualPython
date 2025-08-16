# Dado un número N, primero debe verificar si es primo. Si no es un número primo, 
#imprima el número seguido de dos puntos y luego de un espacio imprime -1. En el caso de que el número sea primo, 
# imprime el número seguido de dos puntos y después de un espacio los primeros 40 decimales de 1/N
N = int(input())


for x in range(3, N):
    if (x%3 == 0):
        print(x, end=":" )
    else:
        print(x, end=" ")
        print(":", -1/N)
        