L = int(input())
T = str(input())
M = []
for linha in range(12):
    vetor = []
    for coluna in range(12):
        vetor.append(float(input()))
    M.append(vetor)
soma = 0
for c in range(12):
    soma += M[L][c]
if T == 'S':
    print(soma)
else:
    med = soma / 12
    print(med)
