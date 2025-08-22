if __name__ == "__main__":

    n, t = map(int, input().split())
    A = list(map(int, input().split()))
    if n == 1:
        total = A[0]
        if t >= 2:
            total += A[0]
        print(total)
        exit()
    
    pref = [0] * n
    pref[0] = A[0]
    for i in range(1, n):
        pref[i] = pref[i-1] + A[i]
    
    def p(i):
        return pref[i] if i >= 0 else 0
    
    mejor = 0
    max_i = min(n - 1, t)
    
    for i in range(max_i + 1):
        rem = t - i
        total = p(i)
        if rem > 0:
            j = max(0, i - rem)
            if i - 1 >= j:
                total += p(i-1) - p(j-1)
        if total > mejor:
            mejor = total
    
    print(mejor)