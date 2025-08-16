def sum_digits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

def generate_series(n):
    
    if n <= 0:
        return []
    
    # Start with first two terms
    prev_prev, prev = 35, 8
    result = [prev_prev]
    
    if n == 1:
        return result
    
    result.append(prev)
    
    # Generate remaining terms
    for i in range(2, n):
        if i % 2 == 0:  # Even position: add previous + two positions back
            current = prev + prev_prev
        else:  # Odd position: sum of digits of previous
            current = sum_digits(prev)
        
        result.append(current)
        prev_prev, prev = prev, current
    
    return result


# Read all input first
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    test_cases.append(n)

# Process and output all results
for n in test_cases:
    series = generate_series(n)
    print('  '.join(map(str, series)))