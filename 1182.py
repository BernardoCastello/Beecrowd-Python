C = int(input())
T = str(input())
M = []
for linha in range(12):
    vetor = []
    for coluna in range(12):
        vetor.append(float(input()))
    M.append(vetor)
soma = 0
for cont in range(12):
    soma += M[cont][C]
if T == 'S':
    print('{:.1f}'.format(soma))
else:
    med = soma / 12
    print('{:.1f}'.format(med))
