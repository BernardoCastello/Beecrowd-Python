n = int(input())
for c in range(n):
    a, b, c = map(str, input().split(' '))
    if len(a) != 2:
        a = '0'+a
    if len(b) != 2:
        b = '0'+b
    if c == '1':
        print(f'{a}:{b} - A porta abriu!')
    else:
        print(f'{a}:{b} - A porta fechou!')
