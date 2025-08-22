import sys

# Precompute the numerators for the first 44 terms
n_max = 44
numerators = [4]  # first term numerator

if n_max > 1:
    # Build Fibonacci sequence
    fib = [0] * (n_max + 10)
    fib[1] = 1
    fib[2] = 1
    for i in range(3, len(fib)):
        fib[i] = fib[i-1] + fib[i-2]
    
    # First two increments: 3 (4->7), 4 (7->11)
    incs = [3, 4]
    # Generate the next 42 increments
    for i in range(2, n_max):
        next_inc = incs[-1] + fib[i]  # fib[2]=1, fib[3]=2, fib[4]=3, ...
        incs.append(next_inc)
    
    # Generate numerators
    for i in range(n_max - 1):
        numerators.append(numerators[-1] + incs[i])

# Read input
data = sys.stdin.read().split()
k = int(data[0])
output_lines = []
idx = 1
for _ in range(k):
    n = int(data[idx])
    idx += 1
    total_sum = 0.0
    for i in range(n):
        term = numerators[i] / (2 * (i + 1))
        total_sum += term
    output_lines.append(f"{total_sum:.4f}")

# Output
print('\n'.join(output_lines))