a, b = map(int, input().split())
t = 0 
for i in range(a):
    r = list(map(int, input().split(' ')))
    aux = 0
    for c in range(len(r)):
        if r[c] == 0:
            break
        else:
            aux += 1
    if aux == b:
        t += 1
        
print(t)
