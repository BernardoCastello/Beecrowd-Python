maior = 0
pos = 0
for c in range(100):
    x = int(input())
    if c == 0:
        maior = x
        pos = c + 1
    else:
        if x > maior:
            maior = x
            pos = c + 1
print(maior)
print(pos)
