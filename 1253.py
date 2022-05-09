n = int(input())
for c in range(n):
    x = list(input())
    v = int(input())
    for i in range(len(x)):
        if ord(x[i]) - v < 65:
            x[i] = chr(91 - (65- abs(ord(x[i]) - v)))
        else:
            x[i] = chr(ord(x[i]) - v)
    for i2 in range(len(x)):
        print(x[i2], end='')
    print()
