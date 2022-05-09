a = int(input())
b = int(input())
c = int(input())

t1 = (b + (2*c))*2
t2 = (2*a) + (2*c)
t3 = ((2*a)+b)*2

if t1 <= t2 and t1 <=t3:
    print(t1)
elif t2 < t1 and t2 <= t3:
    print(t2)
else:
    print(t3)
