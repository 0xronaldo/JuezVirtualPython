import math

# Leer número de casos
K = int(input().strip())
caos = []
for _ in range(K):
    line = input().split()
    N = int(line[0])
    K_val = int(line[1])
    
    total = 0.0
    for i in range(N):
        numerador = i + K_val
        denominador = 2 + i + K_val
        total += numerador / denominador
    
    # Redondear hacia arriba
    caos.append(math.ceil(total))
    
for x in caos:
    print(x)