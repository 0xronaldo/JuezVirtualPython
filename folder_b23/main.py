entrada = input().strip()
result = []

for char in entrada:
    ascii_val = ord(char)
    binary = format(ascii_val, '08b')
    first_4 = binary[:4]
    last_4 = binary[4:]
    
    swapped_binary = last_4 + first_4
    
    swapped_decimal = int(swapped_binary, 2)
    result.append(swapped_decimal)

print(' '.join(map(str, result)))
