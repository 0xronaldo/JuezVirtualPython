num = int(input())
armonico = 0
for _ in range(1, num + 1):
    armonico += 1 / _
print(f"{armonico:.4f}")
