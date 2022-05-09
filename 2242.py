x = str(input())
l1 = []
for c in x:
    if c =='a':
        l1.append(c)
    elif c == 'e':
        l1.append(c)
    elif c == 'i':
        l1.append(c)
    elif c == 'o':
        l1.append(c)
    elif c == 'u':
        l1.append(c)

l2 = list(reversed(l1))
r = 1
for c in range(len(l1)):
    if l1[c] != l2[c]:
        r = 0
        break

if r == 1:
    print('S')
else:
    print('N')
