n = int(input())
t = [0]*3
p = [0]*3
for i in range(n):
    nome = input()
    s1, b1, a1 = input().split(' ')
    t[0] += int(s1)
    t[1] += int(b1)
    t[2] += int(a1)
    s2, b2, a2 = input().split(' ')
    p[0] += int(s2)
    p[1] += int(b2)
    p[2] += int(a2)
ps = (p[0] / t[0]) *100
pb = (p[1] / t[1]) *100
pa = (p[2] / t[2]) *100

print(f'Pontos de Saque: {ps:.2f} %.')
print(f'Pontos de Bloqueio: {pb:.2f} %.')
print(f'Pontos de Ataque: {pa:.2f} %.')
