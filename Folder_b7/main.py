n = int(input())
arr = list(map(int, input().split()))

is_palindrome = True
for i in range(n // 2):
    if arr[i] != arr[n - 1 - i]:
        is_palindrome = False
        break

print("SI" if is_palindrome else "NO")