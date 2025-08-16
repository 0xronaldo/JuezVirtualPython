n = int(input())
for i in range(1, n//2 + 2):
    if (i-1)*2 < n:
        
        print(i, end=' ')
    if (i-1)*2 + 1 < n:
        print(-i,  end=' ')
        