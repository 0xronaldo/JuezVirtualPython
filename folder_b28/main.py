def conteoPicos(heights):
    n = len(heights)
    if n < 3:
        return -1
    peaks = 0
    for i in range(1, n - 1):
        if heights[i] > heights[i-1] and heights[i] > heights[i+1]:
            peaks += 1
    
    return peaks if peaks > 0 else -1
    

if __name__ == "__main__":
    
    k = int(input())
    almacen = []
    for x in range(0,k):
        n = int(input())
        heights = list(map(int, input().split()))
        datos = conteoPicos(heights)
        almacen.append(datos)

for x in almacen:
    print(x)
