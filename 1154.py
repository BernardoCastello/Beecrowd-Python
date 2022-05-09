soma = 0
c = 0
while True:
    x = int(input())
    if x < 0:
        break
    soma += x
    c += 1

print(f'{soma/c:.2f}')
