#!/usr/bin/python3

def max_mushrooms(n, t, mushrooms):
    if t == 0:
        return mushrooms[0]
    
    # Sumas de prefijo y máximo de prefijo
    prefix_sum = [0] * (n + 1)
    prefix_max = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + mushrooms[i]
        prefix_max[i + 1] = max(prefix_max[i], mushrooms[i])
    
    max_mushrooms = mushrooms[0]
    
    # Probar cada punto final del segmento contiguo
    for k in range(1, min(n, t + 1)):
        moves_used = k - 1  # Movimientos para llegar al claro k
        segment_sum = prefix_sum[k]  # Suma de claros 1 a k
        moves_left = t - moves_used  # Movimientos restantes
        
        # Caso 1: Usar el segmento contiguo
        max_mushrooms = max(max_mushrooms, segment_sum)
        
        # Caso 2: Retroceder al claro más valioso en el segmento
        if moves_left >= 1:
            max_in_segment = prefix_max[k]  # Máximo en [0, k-1]
            # Encontrar el índice del claro más valioso
            for i in range(k):
                if mushrooms[i] == max_in_segment:
                    moves_to_i = abs(i - (k - 1))  # Movimientos desde claro k al claro i
                    if moves_to_i <= moves_left:
                        # Verificar regeneración
                        if moves_used + moves_to_i >= i + 2 or i == 0:
                            max_mushrooms = max(max_mushrooms, segment_sum + max_in_segment)
                            break  # Solo necesitamos el primer máximo
    
    # Caso especial: si t >= n-1
    if t >= n - 1:
        total_sum = prefix_sum[n]
        moves_left = t - (n - 1)
        max_mushroom = prefix_max[n]
        extra_mushrooms = (moves_left // 2) * max_mushroom
        max_mushrooms = max(max_mushrooms, total_sum + extra_mushrooms)
    
    return max_mushrooms

# Leer entrada
n, t = map(int, input().split())
mushrooms = list(map(int, input().split()))

# Calcular y mostrar resultado
print(max_mushrooms(n, t, mushrooms))