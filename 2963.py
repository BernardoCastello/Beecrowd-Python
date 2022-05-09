n = int(input())
l = []
for c in range(n):
    y = int(input())
    l.append(y)
maior = max(l)
if l[0] == maior:
    print('S')
else:
    print('N')
