#!/usr/bin/python3

def largest_prime_factor(n):
    largest = -1
    while n % 2 == 0:
        largest = 2
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest = i
            n = n // i
        i += 2
    if n > 1:
        largest = n
    return largest
    
try:
    k = int(input())
    ear = []
    for _ in range(k):
        n = int(input())
        ear.append(largest_prime_factor(n))
    for _ in ear:
        print(_, end='\n')
except EOFError:
    pass
