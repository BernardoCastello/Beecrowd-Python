n = int(input())

menor = 0

for c in range(n):
    a, b = map(float, input().split())
    r = a / b
    if c == 0:
        menor = r
    else:
        if r < menor:
            menor = r
p = menor *1000
print(f'{p:.2f}')
