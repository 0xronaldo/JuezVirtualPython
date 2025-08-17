
if __name__ == "__main__":
    n, m = map(int, input().split())
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().split()))
        matriz.append(fila)

    # Verificar si alguna fila o columna tiene todos los valores iguales
    huye = False
    
    # Verificar filas
    for fila in matriz:
        if all(x == fila[0] for x in fila):
            huye = True
            break
    
    # Verificar columnas
    if not huye:
        for j in range(m):
            columna = [matriz[i][j] for i in range(n)]
            if all(x == columna[0] for x in columna):
                huye = True
                break

    if huye:
        print("HUYE")
    else:
        print("SEGURO")