c1 = 0
c2 = 0
for i in range(6):
    x = float(input())
    if x > 0:
        c1 += 1
        c2 += x
m = c2 /c1
print(f'{c1} valores positivos')
print(f'{m:.1f}')
