#!/usr/bin/python3


entrada = input().strip()
encoded_values = list(map(int, input().strip().split()))
casos = []
for val in encoded_values:
    binary = format(val, '08b')
    first_4 = binary[:4]
    last_4 = binary[4:]
    original_binary = last_4 + first_4
    ascii_val = int(original_binary, 2)
    casos.append(chr(ascii_val))
print(''.join(casos))

