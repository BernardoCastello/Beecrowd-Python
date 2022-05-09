n = int(input())
for c in range(n):
    a, b = map(int, input().split(' '))
    if a > b:
        soma = 0
        for c in range(b + 1, a):
            if c % 2 == 1:
                soma += c
        print(soma)
    else:
        soma = 0
        for c in range(a + 1, b):
            if c % 2 == 1:
                soma += c
        print(soma)
