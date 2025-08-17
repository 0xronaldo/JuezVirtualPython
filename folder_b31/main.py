#!/usr/bin/python3
def lcs_length(s1, s2):
    n, m = len(s1), len(s2)
    # Usar dos filas para optimizar memoria
    dp = [[0] * (m + 1) for _ in range(2)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
    
    return dp[n % 2][m]

k = int(input())
caso = []
for _ in range(k):
    s1 = input().strip()
    s2 = input().strip()
    caso.append(lcs_length(s1, s2))
    
    
for x in caso:
    print(x)