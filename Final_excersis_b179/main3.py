#!/usr/bin/python3
def max_mushrooms(n, t, mushrooms):
    if t == 0:
        return mushrooms[0]
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + mushrooms[i]
    
    max_mushrooms = mushrooms[0]
    max_in_segment = mushrooms[0]
    for k in range(1, min(n, t + 1)):
        moves_used = k - 1  
        segment_sum = prefix_sum[k] 
        moves_left = t - moves_used 
        max_in_segment = max(max_in_segment, mushrooms[k - 1])
        max_mushrooms = max(max_mushrooms, segment_sum)
        if moves_left >= 1:
            for i in range(k):
                moves_to_i = abs(i - (k - 1))
                if moves_to_i <= moves_left:
                    if moves_used + moves_to_i >= i + 2 or i == 0: 
                        max_mushrooms = max(max_mushrooms, segment_sum + mushrooms[i])
    
    if t >= n - 1:
        total_sum = prefix_sum[n]
        moves_left = t - (n - 1)
        max_mushroom = max(mushrooms)
        extra_mushrooms = (moves_left // 2) * max_mushroom  # Cada retroceso toma 2 movimientos
        max_mushrooms = max(max_mushrooms, total_sum + extra_mushrooms)
    
    return max_mushrooms
n, t = map(int, input().split())
mushrooms = list(map(int, input().split()))
print(max_mushrooms(n, t, mushrooms))