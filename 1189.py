t = input()

m=[]
for c in range(12):
    aux = []
    for i in range(12):
        aux.append(float(input()))
    m.append(aux)


soma = 0
a = 0
b = 0
for c2 in range(11):
    if a == 6:
        b =1
        a =5
    for i2 in range(a):
        soma += m[c2][i2]
    if b == 0:
        a +=1
    else:
        a -=1
if t == 'S':
    print('{:.1f}'.format(soma))
else:
    r = soma/30
    print('{:.1f}'.format(r))
