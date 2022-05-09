N, M = (input().split())
n = int(N)
N = [1]*int(N)
M = [1]*int(M)
vi = list(input().split())
c = list(input().split())
clientes = []
tempo = []
for i in range(len(vi)):
    x = N[i] * vi[i]
    tempo.append(int(x))
for i in range(len(c)):
    y = M[i] * c[i]
    clientes.append(int(y))

tempototal = [0]*n
somat = 0
if n == 1:
    for c in range(len(clientes)):
        a = tempototal.index(min(tempototal))
        somat += clientes[c] * tempo[a]
        tempototal[a] += clientes[c] * tempo[a]
    print(somat)
else:
    for c in range(len(clientes)):
        a = tempototal.index(min(tempototal))
        tempototal[a] += clientes[c] * tempo[a]
    print(max(tempototal))
