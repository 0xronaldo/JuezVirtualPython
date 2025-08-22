if __name__ == "__main__":

    # Leer n y t
    n, t = map(int, input().split())
    A = list(map(int, input().split()))
    pref = [0] * n
    pref[0] = A[0]
    for i in range(1, n):
        pref[i] = pref[i-1] + A[i]
    def p(i):
        if i < 0:
            return 0
        return pref[i]
    
    mejor = 0
    max_i = min(n - 1, t) 
    for i in range(max_i + 1):
        tiempo_ida = i
        tiempo_restante = t - tiempo_ida  # para moverse de regreso
        recolecta_ida = p(i)  # hongos en ida: desde 0 hasta i
        recolecta_extra = 0
        
        if tiempo_restante > 0:
            j = max(0, i - tiempo_restante)
            if i - 1 >= j:
                recolecta_extra = p(i - 1) - p(j - 1)
        
        total = recolecta_ida + recolecta_extra
        if total > mejor:
            mejor = total
    
    print(mejor)
    
    