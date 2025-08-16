#!/usr/bin/python3

n = int(input())
casos = []
for _ in range(n):
    time, velocity = map(float, input().split())
    length = time * velocity
    oper = f"{length:.3f}"
#print(f"{length:.3f}")
    casos.append(oper)
    #print(f"{length:.3f}" , end='\n')

for z in casos: 
    print(f"{z}")