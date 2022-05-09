a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

ra = b / c
rb = e / f

if ra > rb:
    print(d)
else:
    print(a)
