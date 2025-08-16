t = int(input())
casos = []
for _ in range(t):
    s = input()
    result = ""
    uppercase = True
    for char in s:
        if char.isalpha():
            if uppercase:
                result += char.upper()
            else:
                result += char.lower()
            uppercase = not uppercase
        else:
            result += char
    casos.append(result)

for _ in casos:
    print(_ ,end='\n')
