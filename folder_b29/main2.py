K = int(input())
acceso = []
for _ in range(K):
    N = int(input()) 
    
    
    monedas = []
    for n in range(1, N + 1):
        valor = 2 * n * n - n  # fórmula: 2n² - n
        monedas.append(str(valor))
    acceso.append(monedas)
    
for x in acceso:
    print(" ".join(x))     