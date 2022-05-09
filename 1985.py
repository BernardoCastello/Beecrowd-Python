n = int(input())
soma = 0
for c in range(n):
    a, b = map(int, input().split())
    if a == 1001:
        x = 1.5 * b
        soma += x
    elif a == 1002:
        x = 2.5 * b
        soma += x
    elif a == 1003:
        x = 3.5 * b
        soma += x
    elif a == 1004:
        x = 4.5 * b
        soma += x
    else:
        x = 5.5 * b
        soma += x
print(f'{soma:.2f}')
