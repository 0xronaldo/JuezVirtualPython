#!/usr/bin/python3
### Oso Juki colecta Hongos en el camino
# @dev Sanchez Ronaldo
# la verdad lo analice hasta que encontre la logica indicada 

def max_Hongos(n, t, mushrooms):
    dp = [[-float('inf')] * (t + 1) for _ in range(n)]
    
    dp[0][0] = mushrooms[0]
    
    for j in range(t):
        for i in range(n):
            if dp[i][j] == -float('inf'):
                continue
                
            
            if i + 1 < n:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + mushrooms[i + 1])
                
            
            if i > 0:
                dp[i - 1][j + 1] = max(dp[i - 1][j + 1], dp[i][j] + mushrooms[i - 1])
                
            # Considerar regeneración: si estamos en el claro i, podemos recolectar de nuevo
            # si han pasado al menos 2 movimientos desde la última recolección
            # Para simplificar, asumimos que cada claro se recolecta una vez por visita
            # y verificamos retrocesos en el bucle principal
    
    
    max_mushrooms = max(dp[i][t] for i in range(n) if dp[i][t] != -float('inf'))
    
    for i in range(n):
        if dp[i][t] == -float('inf'):
            continue
        for k in range(n):
            moves_needed = abs(i - k)
            if j + moves_needed <= t:
                    dp[k][j + moves_needed] = max(dp[k][j + moves_needed], dp[i][j] + mushrooms[k])
    
    max_mushrooms = max(max_mushrooms, max(dp[i][j] for i in range(n) for j in range(t + 1) if dp[i][j] != -float('inf')))
    
    return max_mushrooms


n, t = map(int, input().split())
mushrooms = list(map(int, input().split()))
print(max_Hongos(n, t, mushrooms))



#*
#def max_mushrooms(n, t, mushrooms):
    # dp[i][j] = máxima cantidad de hongos después de j movimientos, en el claro i
    #dp = [[-float('inf')] * (t + 1) for _ in range(n)]
    
    # Inicialización: Juki empieza en el claro 1 (índice 0), recolecta en t=0
    #dp[0][0] = mushrooms[0]
    
    # Para cada numero de movimientos
    #for j in range(t):
        #for i in range(n):  # Para cada claro
            #if dp[i][j] == -float('inf'):
            #    continue
                
            # Moverse al claro siguiente (i+1) si es posible
            #if i + 1 < n:
            #    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + mushrooms[i + 1])
                
            # Moverse al claro anterior (i-1) si es posible
            #if i > 0:
                #dp[i - 1][j + 1] = max(dp[i - 1][j + 1], dp[i][j] + mushrooms[i - 1])
                
            # Considerar regeneración: si estamos en el claro i, podemos recolectar de nuevo
            # si han pasado al menos 2 movimientos desde la última recolección
            # Para simplificar, asumimos que cada claro se recolecta una vez por visita
            # y verificamos retrocesos en el bucle principal
    
    # Encontrar el máximo después de t movimientos
    #max_mushrooms = max(dp[i][t] for i in range(n) if dp[i][t] != -float('inf'))
    
    # Considerar recolección adicional después del último movimiento
    # Si Juki regresa a un claro donde los hongos han regenerado
    #for i in range(n):
        #if dp[i][t] == -float('inf'):
        #    continue
        # Probar retroceder a claros anteriores donde los hongos han regenerado
        #for k in range(n):
            # Calcular movimientos necesarios para llegar al claro k
            #moves_needed = abs(i - k)
            #if j + moves_needed <= t:
                # Verificar si los hongos en el claro k han regenerado
                # Necesitamos al menos 2 movimientos desde la última recolección
                # Para simplificar, asumimos que la recolección adicional ocurre al final
                #if moves_needed >= 2 or k != i:  # Evitar contar el mismo claro sin regeneración
                #    dp[k][j + moves_needed] = max(dp[k][j + moves_needed], dp[i][j] + mushrooms[k])
    
    # Encontrar el máximo global
    #max_mushrooms = max(max_mushrooms, max(dp[i][j] for i in range(n) for j in range(t + 1) if dp[i][j] != -float('inf')))
    
    #return max_mushrooms

# Leer entrada
#n, t = map(int, input().split())
#mushrooms = list(map(int, input().split()))

# Calcular y mostrar resultado
#print(max_mushrooms(n, t, mushrooms))
#