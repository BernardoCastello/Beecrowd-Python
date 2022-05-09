while True:
    a, b = map(int, input().split())
    if a <= 0 or b <= 0:
        break
    soma = 0
    if a > b:
        for c in range(b, a + 1):
            soma += c
            print(c, end=' ')
        print(f'Sum={soma}')
    else:
        for c in range(a, b + 1):
            soma += c
            print(c, end=' ')
        print(f'Sum={soma}')
