t = input()

m=[]
for c in range(12):
    aux = []
    for i in range(12):
        aux.append(float(input()))
    m.append(aux)


soma = 0
a = 11
for c2 in range(11):
    for i2 in range(a):
        soma += m[c2][i2]
    a = a -1
if t == 'S':
    print('{:.1f}'.format(soma))
else:
    r = soma/66
    print('{:.1f}'.format(r))
