soma = 0
c = 0
while True:
    x = float(input())
    if 0 <= x <= 10:
        soma += x
        c += 1
    else:
        print('nota invalida')
    if c == 2:
        break
print(f'media = {soma/2:.2f}')
