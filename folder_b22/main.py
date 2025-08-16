
if __name__ == "__main__":
    
    entrada = input().split()
    target_sum = int(entrada[0])
    n = int(entrada[1])

    numbers = list(map(int, input().split()))
    
    
    def count_subsets_with_sum(target_sum, numbers):
        count = 0
        n = len(numbers)
        for i in range(2**n):
            subset_sum = 0
            for j in range(n):
                # Check if j-th bit is set in i
                if i & (1 << j):
                    subset_sum += numbers[j]
            
            if subset_sum == target_sum:
                count += 1
        
        return count
    
    result = count_subsets_with_sum(target_sum, numbers)
    print(result)

# Read input

