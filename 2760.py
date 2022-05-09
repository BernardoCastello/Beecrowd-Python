a = input()
b = input()
c = input()
print(a + b + c)
print(b + c + a)
print(c + a + b)
a = list(a)
b = list(b)
c = list(c)
if len(a) > 10:
    for c1 in range(10):
        print(a[c1], end='')
else:
    for c1 in range(len(a)):
        print(a[c1], end='')
if len(b) > 10:
    for c2 in range(10):
        print(b[c2], end='')
else:
    for c2 in range(len(b)):
        print(b[c2], end='')
if len(c) > 10:
    for c3 in range(10):
        print(c[c3], end='')
else:
    for c3 in range(len(c)):
        print(c[c3], end='')
print()
