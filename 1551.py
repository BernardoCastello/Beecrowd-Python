n = int(input())
for c in range(n):
    lista = [0]*26
    frase = list(input())
    cont = 0
    for c in range(len(frase)):
        aux = ord(frase[c])
        if 122 >= aux >= 97 and lista[97-aux] == 0:
            lista[97-aux] = 1
            cont += 1
    if cont < 13:
        print('frase mal elaborada')
    elif 13 <= cont < 26:
        print('frase quase completa')
    else:
        print('frase completa')
