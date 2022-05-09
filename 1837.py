a, b = map(int, input().split(' '))
if b>0:
    r1 =  a//b
    r2 = a%b
else:
    b *= -1
    r1 =  (a//b)*(-1)
    r2 = a%b
print(r1, r2)
