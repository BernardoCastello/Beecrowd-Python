n = int(input())
for c in range(n):
    a, b = input().split()
    a = list(a)
    b = list(b)
    f = []
    if len(a) >= len(b):
        for c2 in range(len(a)):
            f.append(a[c2])
            if c2 < len(b):
                f.append(b[c2])
    else:
        for c3 in range(len(b)):
            if c3 < len(a):
                f.append(a[c3])
            f.append(b[c3])
    print(''.join(f))
