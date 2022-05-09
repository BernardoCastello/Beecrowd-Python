x = int(input())
for c in range(x):
    n = int(input())
    v = 1
    for c in range(2, n):
        if n % c == 0:
            print(f'{n} nao eh primo')
            v = 0
            break
    if v == 1:
        print(f'{n} eh primo')
