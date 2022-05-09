n = int(input())
for c in range(n):
    x = input()
    y = input()
    if x == 'ataque':
        if y == 'ataque':
            print('Aniquilacao mutua')
        elif y == 'pedra':
            print('Jogador 1 venceu')
        else:
            print('Jogador 1 venceu')
    elif x == 'pedra':
        if y == 'ataque':
            print('Jogador 2 venceu')
        elif y == 'pedra':
            print('Sem ganhador')
        else:
            print('Jogador 1 venceu')
    elif x == 'papel':
        if y == 'ataque':
            print('Jogador 2 venceu')
        elif y == 'pedra':
            print('Jogador 2 venceu')
        else:
            print('Ambos venceram')
