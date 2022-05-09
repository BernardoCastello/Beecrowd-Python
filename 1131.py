vg = 0
vi = 0
em = 0

while True:
    a, b = map(int, input().split())
    if a>b:
        vi += 1
    elif b>a:
        vg += 1
    else:
        em += 1
    print('Novo grenal (1-sim 2-nao)')
    r = int(input())
    if r == 2:
        break
print(f'{vg + vi + em} grenais')
print(f'Inter:{vi}')
print(f'Gremio:{vg}')
print(f'Empates:{em}')
if vi > vg:
    print('Inter venceu mais')
elif vg > vi:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
