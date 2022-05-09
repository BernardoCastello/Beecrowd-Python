a, b = map(int, input().split())
if a == b:
    print('O JOGO DUROU 24 HORA(S)')
elif a > b:
    r  = 24 - a + b
    print(f'O JOGO DUROU {r} HORA(S)')
else:
    r = b - a
    print(f'O JOGO DUROU {r} HORA(S)')
