


#!/usr/bin/python3

K = int(input())
casos = []
for _ in range(K):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    median = -1
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 1:
        mid_index = n // 2
        candidate = numbers[mid_index]
        greater = sum(1 for x in numbers if x > candidate)
        lesser = sum(1 for x in numbers if x < candidate)
        # Verificar que hay exactamente N//2 elementos mayores y menores
        if greater == lesser == mid_index:
            median = candidate
    casos.append(median)

for x in casos:    
    print(x, end='\n')

#K = int(input())
#casos = []
#for _ in range(K):
#    N = int(input())
#    numbers = list(map(int, input().split()))
#    
#    median = -1
#    numbers.sort()
#    n = len(numbers)
#    
#    if n % 2 == 1:
#        mid_index = n // 2
#        candidate = numbers[mid_index]
#        greater = sum(1 for x in numbers if x > candidate)
#        lesser = sum(1 for x in numbers if x < candidate)
#        if greater == lesser:
#            median = candidate
#    casos.append(median)

#for x in casos:    
#    print(x, end='\n')
"""
Resultado de la ejecución
Entrada 
=================
3
5
2 4 5 6 7
5
1 2 2 3 4
5
2 3 3 3 4
=================
Respuesta Correcta:
5
-1
-1
-----------------
Tu respuesta:
5
-1
3

=================

Este modulo esta en modo beta. No se confi 

Dato esperado '-', Tu salida '3'. 
"""