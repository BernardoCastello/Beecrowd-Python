a = int(input())
b = int(input())
maior = 0
menor = 0
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
soma = 0
for c in range(menor + 1, maior):
    if c % 2 != 0:
        soma += c
print(soma)
