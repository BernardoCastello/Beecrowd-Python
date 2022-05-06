a, b = map(float, input().split())
c, d = map(float, input().split())
r = (((c - a)**2) + ((d - b)**2))**(1/2)
print(f'{r:.4f}')
