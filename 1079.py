par = []
impar = []
for c in range(0, 15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    if x % 2 != 0:
        impar.append(x)
    if len(par) == 5:
        for p in range (0, 5):
            print('par[{}] = {}'.format(p, par[p]))
        par = []
    if len(impar) == 5:
        for i in range (0, 5):
            print('impar[{}] = {}'.format(i, impar[i]))
        impar = []
if len(impar) != 0:
    for i2 in range(0, len(impar)):
        print('impar[{}] = {}'.format(i2, impar[i2]))
if len(par) != 0:
    for p2 in range(0, len(par)):
        print('par[{}] = {}'.format(p2, par[p2]))
