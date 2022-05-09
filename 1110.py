while True:
    n = int(input())
    if n == 0:
        break
    else:
        baralho = []
        for c in range(n, 0, -1):
            baralho.append(c)
        
        descarte = []

        for c in range(n - 1):
            descarte.append(baralho[-1])
            baralho.pop()
            baralho.insert(0,baralho[-1])
            baralho.pop()
        
    print('Discarded cards: ', end='')
    for c in range(len(descarte)):
        if c == len(descarte) - 1:
            print(f'{descarte[c]}')
            break
        print(f'{descarte[c]}, ', end='')
    print(f'Remaining card: {baralho[0]}')
