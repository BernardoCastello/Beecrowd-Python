n = int(input())
letras = ['F', 'A', 'C', 'E']
cont = 0
for i in range(n):
    aux = list(input().replace(' ', ''))
    v = 1
    for c in range(1, 5):
        if letras[-c] != aux[c-1]:
            v = 0
            break
    if v == 1:
        cont += 1
        for c in range(4):
            letras.pop()
    else:
        for c in range(4):
            letras.append(aux[c])
    if len(letras) == 0:
        letras = ['F', 'A', 'C', 'E']
print(cont)
