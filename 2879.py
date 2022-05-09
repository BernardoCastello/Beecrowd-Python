n = int(input())
lista = []
for c in range(n):
    lista.append(int(input()))
r = n - lista.count(1)
print(r)
