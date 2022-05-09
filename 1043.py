a, b, c = map(float, input().split(' '))
x = 0
if a < b + c:
    if b < a + c:
        if c < b + a:
            x = 1
if x == 1:
    p = a + b + c
    print(f'Perimetro = {p:.1f}')
else:
    area = ((a+b)*c)/2
    print(f'Area = {area:.1f}')
