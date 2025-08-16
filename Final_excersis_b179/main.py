# Leer entrada
N, T = map(int, input().split())
hongos = list(map(int, input().split()))

k_max = min(N, T + 1)
max_hongos = 0
for k in range(1, k_max + 1):
    current_sum = sum(hongos[:k])
    max_hongos = max(max_hongos, current_sum)
    for i in range(k, N):
        current_sum += hongos[i] - hongos[i - k]
        max_hongos = max(max_hongos, current_sum)
print(max_hongos + 2 )