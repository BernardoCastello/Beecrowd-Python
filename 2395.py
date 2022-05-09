x, y, z = input().split(' ')
a, b, c = input().split(' ')

r1 = int(a) // int(x)
r2 = int(b) // int(y)
r3 = int(c) // int(z)

rf = r1 * r2 * r3

print(rf)
