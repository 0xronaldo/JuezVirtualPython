def primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def digitos_decimales(n, c):
    digits = []
    remainder = 1
    for _ in range(c):
        remainder *= 10
        digit = remainder // n
        digits.append(str(digit))
        remainder = remainder % n
    return digits
casos = []
t = int(input())
for _ in range(t):
    n = int(input())
    casos.append(n)

for n in casos:
    if primo(n):
        digits = digitos_decimales(n, 40)
        print(f"{n}: {' '.join(digits)} ", end="\n")
    else:
        print(f"{n}: -1")
