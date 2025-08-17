#!/usr/bin/python3

K = int(input())

almacen = []
for _ in range(K):
    A, B = map(int, input().split())
    distancia = abs(A - B)
    almacen.append(distancia)
    #print(distancia)
#print(" ".join(map(int, almacen)))
for _ in almacen:
    print(_ , end='\n')