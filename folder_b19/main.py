A, B = map(int, input().split())

if (A % B == 0):
    print(f"{A} es divisible por {B}")
elif (B % A == 0):
    print(f"{B} es divisible por {A}")
else:
    print("-1")
