#!/usr/bin/python3

if __name__ == "__main__":
    n, t = map(int, input().split())
    mushrooms = list(map(int, input().split()))
        
    if t == 0:
        print(mushrooms[0])
    else:
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + mushrooms[i]
        max_mushrooms = mushrooms[0]
        for k in range(1, min(n, t + 1)):
            moves_used = k - 1
            segment_sum = prefix_sum[k]
            moves_left = t - moves_used
            
            max_mushrooms = max(max_mushrooms, segment_sum)
            if moves_left >= 1:
                for i in range(max(0, k - 3), k):
                    moves_to_i = abs(i - (k - 1))
                    if moves_to_i <= moves_left:
                        if moves_used + moves_to_i >= i + 2 or i == 0:
                            max_mushrooms = max(max_mushrooms, segment_sum + mushrooms[i])
        if t >= n - 1:
            total_sum = prefix_sum[n]
            moves_left = t - (n - 1)
            max_mushroom = max(mushrooms)
            extra_mushrooms = (moves_left // 2) * max_mushroom
            max_mushrooms = max(max_mushrooms, total_sum + extra_mushrooms)
        
        print(max_mushrooms)
