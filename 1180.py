M = []
N = int(input())
M.append(list(map(int, input().split())))
menor = 0
for c in range(N):
    if c == 0:
        menor = M[0][0]
    else:
        if menor > M[0][c]:
            menor = M[0][c]
print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(M[0].index(menor)))
