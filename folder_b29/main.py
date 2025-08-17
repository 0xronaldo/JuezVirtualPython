def tamano_monedas(n):
    if n == 0:
        return 0
    return n * (n + 1) * (n + 2) // 6

k = int(input())
acceso = []
for _ in range(k):
    n = int(input())
    if n == 0:
        print()
    else:
        almacen = []
        #result = []
        for i in range(1, n + 1):
            almacen.append(str(tamano_monedas(i)))
        acceso.append(almacen)

#print(" ".join(acceso))
for x in acceso:
    print(" ".join(x))       