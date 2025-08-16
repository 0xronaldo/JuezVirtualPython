#!/usr/bin/python3

# suma de cubos : 

t = int(input())
casos = []
for _ in range(t):
    n = int(input())
    found = False
    max_val = int(n**(1/3)) + 1
    cubes = [i**3 for i in range(max_val + 1)]
    #casos.append(cubes)
    for a in range(max_val + 1):
        if cubes[a] > n:
            break
        for b in range(max_val + 1):
            if cubes[a] + cubes[b] > n:
                break
            remaining = n - cubes[a] - cubes[b]
            c = int(remaining**(1/3) + 0.5)
            if c >= 0 and c**3 == remaining:
                found = True
                break
        if found:
            break
    if found:
        casos.append("SI")
    else:
        casos.append("NO")
#    for _ in range(casos):

        #print("SI" if found else "NO")

for _ in casos:
    print(_, end='\n')

#print("SI" if found else "NO")
