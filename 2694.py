n = int(input())

for c in range(n):
    f = input()
    p1 = int(f[2]+f[3])
    p2 = int(f[5]+f[6]+f[7])
    p3 = int(f[11]+f[12])
    t = p1 + p2 + p3
    print(t)
