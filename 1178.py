lista = []
n = float(input())
for c in range(0, 100):
    lista.append(n)
    n = n / 2
for c in range(0, 100):
    print('N[{}] = {:.4f}'.format(c, lista[c]))
