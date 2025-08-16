#!/usr/bin/python3
X, Y = map(int, input().split())

mayor = max(X, Y)
menor = min(X, Y)

for x in range(mayor, menor - 1, -1):
    print(x)
