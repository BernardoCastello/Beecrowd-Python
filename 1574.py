n = int(input())
for i in range(n):
    lista = [0]
    x = int(input())
    for c in range(x):
        r = input()
        if r == 'RIGHT':
            lista.append(1)
        elif r == 'LEFT':
            lista.append(-1)
        else:
            r = r.split(' ')
            r = int(r[-1])
            lista.append(lista[r])
    soma = 0
    for c2 in range(len(lista)):
        soma += lista[c2]
    print(soma)
